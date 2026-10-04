from django.core.cache import cache

from config.settings import CACHES_ENABLED
from .models import Product, Category


def get_product_list_from_cache():
    """ Получает список продуктов из кэша, если кэш пустой, обращается к базе данных. """

    if not CACHES_ENABLED:
        return Product.objects.all()

    key = "product_list"
    products = cache.get(key)
    if products.exists():
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

CACHE_TIMEOUT = 60 * 15 # caсhe - 15 минут

def get_products_by_category(category_id):
    cache_key = f'category_{category_id}_products'
    products = cache.get(cache_key)

    if products is None:
        try:
            category = Category.objects.get(id=category_id)
            products = list(Product.objects.filter(category=category))
            cache.set(cache_key, products, CACHE_TIMEOUT)
        except Category.DoesNotExist:
            return []
    return products