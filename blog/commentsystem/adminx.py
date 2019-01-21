__date__ = '$DATE %TIME'
import xadmin
from commentsystem.models import Comments


class CommentsAdmin(object):
    list_display = ['user', 'blog', 'content', 'date']
    list_fields = ['user', 'blog', 'content', 'date']
    search_fields = ['user', 'blog', 'content']


xadmin.site.register(Comments, CommentsAdmin)
