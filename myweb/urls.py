"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Post
from myweb.settings import MEDIA_ROOT

from blog import views as blog_views

# sitemap
info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'published_data'

}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace="blog")),
    re_path(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 图片文件加载路径
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
            name='django.contrib.sitemaps.views.sitemap'),
]

handler403 = blog_views.permisson_denied
handler404 = blog_views.page_not_found
