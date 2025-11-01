from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("products_list/", views.products_list, name="products_list"),
    path("products/<int:pk>/", views.products_detail, name="products_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
