from django.db import models

from users.models import CustomUser


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовать")

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = [
            "name",
            "price",
        ]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]


class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование организации")
    email = models.CharField(max_length=100, verbose_name="Электронная почта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"
        ordering = [
            "name",
        ]
