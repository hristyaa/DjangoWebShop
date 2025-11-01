from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Add test products to the database and load test data from fixture'

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Test Category')
        # category1, _ = Category.objects.get_or_create(name='Смартфоны')
        # category2, _ = Category.objects.get_or_create(name='Телевизоры')

        products = [
            {'name': 'Test Product', 'price': 100, 'category': category},
            {'name': 'Test Product 2', 'price': 200, 'category': category},
            ]

        for products_data in products:
            product, created = Product.objects.get_or_create(**products_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {product.name}'))

        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))






