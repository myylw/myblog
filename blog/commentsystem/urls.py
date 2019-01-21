from django.urls import path
from .views import CommentCreateView

urlpatterns = [
    path('add_comment/', CommentCreateView.as_view(), name='CommentCreateView'),

]
