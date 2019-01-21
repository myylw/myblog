from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, FormView, DetailView, ListView

from commentsystem.models import Comments
from .forms import UserCreateForm, UserLoginForm
from .models import Blogs


class UserRegView(FormView):
    form_class = UserCreateForm
    template_name = 'reg.html'
    success_url = reverse_lazy('indexpage')

    def form_valid(self, form):
        form.save()
        return super(UserRegView, self).form_valid(form)


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('indexpage')

    def form_valid(self, form):
        user_cache = form.user_cache
        if user_cache is not None and user_cache.is_active:
            login(self.request, user_cache)
            return super(UserLoginView, self).form_valid(form)
        else:
            return HttpResponseRedirect(reverse('UserLoginView'))


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('indexpage'))


class ChangPasswordView(PasswordChangeView):
    template_name = 'changepwd.html'
    success_url = reverse_lazy('indexpage')


class ResetPasswordView(FormView):
    form_class = PasswordResetForm
    template_name = 'resetpwd.html'


class BlogListView(ListView):
    model = Blogs
    template_name = 'list.html'
    context_object_name = 'blogs'
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        order = super(BlogListView, self).get_queryset()
        print(order)
        kw = self.kwargs.get('sort')
        if kw == 'T':
            return order.order_by('-create_date')
        elif kw == 'H':
            return order.order_by('-views')
        else:
            return order


class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        blog = super(BlogDetailView, self).get_object(self.queryset)
        self.bid = blog.id
        blog.views += 1
        blog.save()
        print(blog)
        return blog

    def get_context_data(self, **kwargs):
        content = super(BlogDetailView, self).get_context_data(**kwargs)
        comments = Comments.objects.filter(blog=self.bid)
        print(comments)
        content['comments'] = comments
        return content
