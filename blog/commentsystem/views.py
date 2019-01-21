from django.shortcuts import HttpResponse
from django.views.generic import View
from .forms import CommentCreateForm


class CommentCreateView(View):
    def post(self, request):
        print(request.POST)
        comment_form = CommentCreateForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail"}', content_type='application/json')



