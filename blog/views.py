from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import BlogPost
from config import settings


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

        if self.post.count_of_views == 100:
            self.send_to_email()

        self.post.save()
        return self.post

    def send_to_email(self):
        subject='Пост набрал 100 просмотров!'
        message = f"Поздравляем! Ваш пост '{self.post.title}' набрал 100 просмотров!"

        send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
        print(f"Письмо на email отправлен для статьи: {self.post.title}")


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blog:posts_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blog:posts_list')

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:posts_list')





