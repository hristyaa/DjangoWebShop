from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст, поулчает данные из базы данных."""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get('products_list')
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set('products_list', products)
    return products

