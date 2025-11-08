from django.shortcuts import render
from django.views.generic import ListView

from blog.models import BlogPost


class BlogPostsListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_posts_list.html'
    context_object_name = 'blog_posts'
