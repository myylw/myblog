from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    nick_name = models.CharField(max_length=100, verbose_name='Nick Name')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class Blogs(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    views = models.IntegerField(default=0)

    def view_add_one(self):
        self.views += 1
    class Meta:
        verbose_name='博客'
        verbose_name_plural=verbose_name

# class Like(models.Model):
#     count = models.IntegerField(default=0)
#     blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)


# class Comment(models.Model):
#     uid = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment_content = models.TextField(null=False, blank=False)
#     create_date = models.DateTimeField(auto_now_add=True)
