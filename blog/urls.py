from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from blog.apps import BlogConfig
from blog.views import BlogPostsListView

# from . import views


app_name = BlogConfig.name

urlpatterns = [
    path("blog/", BlogPostsListView.as_view(), name="posts_list"),
    # path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    # path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
