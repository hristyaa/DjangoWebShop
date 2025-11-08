from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView

# from . import views


app_name = BlogConfig.name

urlpatterns = [
    path("posts/", BlogPostListView.as_view(), name="posts_list"),
    path("posts/<int:pk>/", BlogPostDetailView.as_view(), name="post_detail"),
    path("posts/create/", BlogPostCreateView.as_view(), name="post_create"),
    path("posts/update/<int:pk>/", BlogPostUpdateView.as_view(), name="post_update"),
    # path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
