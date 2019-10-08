from django.db import models
from ckeditor.fields import RichTextField
import django.utils.timezone as timezone


# Create your models here.
# ---------------------------------------------------用户表
class LoginUser(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    email = models.CharField(max_length=32, verbose_name='邮箱')
    phone_number = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    photo = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='图像')
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄')
    gender = models.CharField(max_length=4, null=True, blank=True, verbose_name='性别')
    address = models.TextField(null=True, blank=True, verbose_name='地址')
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'LoginUser'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


# ---------------------------------------------作者表
class Author(models.Model):

    name = models.CharField(max_length=32, verbose_name='作者名字')
    age = models.IntegerField(verbose_name='年龄')
    gender = models.IntegerField(choices=((1, '男'), (2, '女')), verbose_name='性别', default=1)
    email = models.CharField(max_length=32, verbose_name='电子邮件')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name


# -------------------------文章类型表
class Type(models.Model):
    name = models.CharField(max_length=32, verbose_name='名字')
    description = models.TextField(verbose_name='描述')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type'
        verbose_name = '类型'
        verbose_name_plural = verbose_name


# ----------------------------------文章表
class Article(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    date = models.DateField(verbose_name='日期', default=timezone.now)
    content = models.TextField()
    # content = RichTextField()
    description = models.TextField()
    # description = RichTextField()
    # 图片类型
    # upload_to指定文件上传位置，需要和static下的路径相同
    picture = models.ImageField(upload_to='images')
    # 推荐和点击率
    recommend = models.IntegerField(verbose_name='推荐', default=0)
    click = models.IntegerField(verbose_name='点击率', default=0)
    author = models.ForeignKey(to=Author, on_delete=models.SET_DEFAULT, default=1)
    type = models.ForeignKey(to=Type, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
