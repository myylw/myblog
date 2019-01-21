from django.forms import ModelForm
from .models import Comments


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content', 'user', 'blog']
