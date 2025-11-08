from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    preview = models.ImageField(upload_to="blog_images/", verbose_name="Превью", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    count_of_views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.title} {self.created_at} {self.count_of_views}"

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = [
            "title",
            "created_at",
        ]
