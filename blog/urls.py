from django.urls import path, re_path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('post/<int:blog_id>/', views.post_detail, name="post_detail"),
    re_path(r'^category/(?P<category_id>.*)$', views.category, name="post_category"),
    re_path(r'^tag/(?P<tag_id>.*)$', views.post_tag, name="post_tag"),
    path('about/', views.about, name="about")
]
