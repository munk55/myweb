from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category, Tag
# Create your views here.
import markdown
import pygments


def make_paginator(objects, page, num=5):
    """  分页 """
    paginator = Paginator(objects, num)
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return object_list, paginator






def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', locals())


def post_detail(request, blog_id):
    post = get_object_or_404(Post, id=blog_id)
    # markdown配置
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc

    return render(request, 'blog/post_detail.html', locals())


def category(request, category_id):
    c = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=c)

    return render(request, 'blog/index.html', locals())


def post_tag(request, tag_id):
    t = Tag.objects.get(id=tag_id)
    if t.name == "全部":
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(tags=t)

    return render(request, 'blog/index.html', locals())


def about(request):
    return render(request, 'blog/about.html')


def permisson_denied(request):
    return render(request, 'blog/403.html', locals())


def page_not_found(request):
    return render(request, 'blog/404.html', locals())