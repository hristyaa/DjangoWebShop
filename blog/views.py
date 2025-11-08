from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        self.post = super().get_object(queryset)
        self.post.count_of_views += 1
        self.post.save()
        return self.post





