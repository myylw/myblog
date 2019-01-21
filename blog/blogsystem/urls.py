from django.urls import path, re_path
from .views import UserRegView, UserLoginView, UserLogoutView, BlogListView, BlogDetailView, ChangPasswordView, \
    ResetPasswordView

urlpatterns = [
    path('reg/', UserRegView.as_view(), name='UserRegView'),
    path('login/', UserLoginView.as_view(), name='UserLoginView'),
    path('logout/', UserLogoutView.as_view(), name='UserLogoutView'),
    path('hot/', BlogListView.as_view(), {'sort': 'H'}, name='BlogHotListView'),
    path('', BlogListView.as_view(), {'sort': 'T'}, name='BlogListView'),
    re_path('(?P<pk>[0-9]+)/blog', BlogDetailView.as_view(), name='BlogDetailView'),
    path('change/', ChangPasswordView.as_view(), name='ChangePasswordView'),
    path('reset/', ResetPasswordView.as_view(), name='ResetPasswordView'),

]
