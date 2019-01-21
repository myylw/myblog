from django.db import models
from blogsystem.models import User, Blogs


class Comments(models.Model):
    content = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content


