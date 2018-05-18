from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"博客分类", null=True, blank=True)

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"博客标签")

    class Meta:
        verbose_name = u"博客标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name=u"标题")
    author = models.ForeignKey('auth.User', verbose_name=u"博客作者", on_delete=models.CASCADE)
    body = models.TextField(verbose_name=u"博客正文")
    images = models.ImageField(upload_to='blog/images', null=True, blank=True, verbose_name=u"博客配图")
    category = models.ForeignKey(Category, verbose_name=u"博客分类", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u"标签")
    excerpt = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"博客摘要")
    visiting = models.PositiveIntegerField(default=0, verbose_name=u"访问量")
    created_data = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")
    published_data = models.DateTimeField(auto_now=True, verbose_name=u"修改时间")

    class Meta:
        ordering = ['-created_data']
        verbose_name = u"博客文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
    # 每篇文章的连接地址

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'blog_id': self.id})
