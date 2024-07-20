import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Открываем файл с фикстурами категорий и загружаем данные в формате JSON
        category_fixture_path = os.path.join(
            settings.BASE_DIR, "catalog/fixtures/category.json"
        )
        with open(category_fixture_path, "r", encoding="utf-8") as file:
            categories = json.load(file)
        return categories

    @staticmethod
    def json_read_products():
        # Открываем файл с фикстурами продуктов и загружаем данные в формате JSON
        product_fixture_path = os.path.join(
            settings.BASE_DIR, "catalog/fixtures/product.json"
        )
        with open(product_fixture_path, "r", encoding="utf-8") as file:
            products = json.load(file)
        return products

    def handle(self, *args, **options):
        # Удаляем все продукты из базы данных
        Product.objects.all().delete()
        # Удаляем все категории из базы данных
        Category.objects.all().delete()

        # Создаем списки для хранения объектов категорий и продуктов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    name=category["fields"]["name"],
                    description=category["fields"]["description"],
                    pk=category["pk"],
                )
            )

        # Создаем объекты категорий в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)
        self.stdout.write(self.style.SUCCESS("Successfully loaded categories."))

        # Обходим все значения продуктов из фикстуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    name=product["fields"]["name"],
                    description=product["fields"]["description"],
                    price=product["fields"]["price"],
                    photo=product['fields'].get("photo", ""),
                    created_at=product["fields"]["created_at"],
                    updated_at=product["fields"]["updated_at"],
                    category=Category.objects.get(pk=category["pk"]),
                )
            )

        # Создаем объекты продуктов в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
        self.stdout.write(self.style.SUCCESS("Successfully loaded products."))
