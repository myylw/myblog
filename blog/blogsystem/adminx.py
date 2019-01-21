__date__ = '$DATE %TIME'
import xadmin
from blogsystem.models import Blogs
from xadmin import views


class BlogsAdmin(object):
    list_display = ['title', 'body', 'views', 'create_date']
    list_fields = ['title', 'body', 'views', 'create_date']
    search_fields = ['title', 'body', 'views']


class GlobalSetting(object):
    site_title = "快乐博客后台管理系统"
    site_footer = "http://www.baidu.com"


xadmin.site.register(views.CommAdminView, GlobalSetting)

xadmin.site.register(Blogs, BlogsAdmin)
