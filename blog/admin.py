from django.contrib import admin

from blog.models import BlogPost
# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "created_at",
    )
    search_fields = (
        "id",
        "title",
        "created_at",
    )

