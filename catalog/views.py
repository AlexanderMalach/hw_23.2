# catalog/views.py
from django.shortcuts import render

from catalog.models import Product


def index(request):
    # Получаем последние пять товаров
    latest_products = Product.objects.all().order_by('-created_at')[:5]

    # Выводим последние пять товаров в консоль
    for product in latest_products:
        print(f'Product: {product.name}, Created at: {product.created_at}')

    # Передаем последние пять товаров в контекст шаблона
    context = {'latest_products': latest_products}
    return render(request, 'catalog/index.html', context)
