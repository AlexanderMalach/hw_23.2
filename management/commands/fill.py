import json
from pathlib import Path
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Load data from JSON files and populate the database, clearing old data first'

    @staticmethod
    def json_read_categories(data):
        # Получаем данные категорий из общего JSON
        return [item for item in data if item['model'] == 'catalog.category']

    @staticmethod
    def json_read_products(data):
        # Получаем данные продуктов из общего JSON
        return [item for item in data if item['model'] == 'catalog.product']

    def handle(self, *args, **options):
        # Определите путь к файлу JSON относительно текущей директории
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        json_path = base_dir / 'catalog' / 'fixtures' / 'catalog.json'

        # Читаем данные из файла JSON
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Удалить все продукты
        Product.objects.all().delete()
        # Удалить все категории
        Category.objects.all().delete()

        # Создать списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Получаем данные категорий и продуктов из общего JSON
        categories = Command.json_read_categories(data)
        products = Command.json_read_products(data)

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for category_data in categories:
            fields = category_data['fields']
            category_for_create.append(
                Category(
                    id=category_data['pk'],  # предполагается, что JSON содержит первичный ключ
                    name=fields['name'],
                    description=fields.get('description', '')
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фикстуры для получения информации об одном объекте
        for product_data in products:
            fields = product_data['fields']
            product_for_create.append(
                Product(
                    id=product_data['pk'],  # предполагается, что JSON содержит первичный ключ
                    name=fields['name'],
                    price=fields['price'],
                    description=fields.get('description', ''),
                    category=Category.objects.get(pk=fields['category'])
                    # получаем категорию из базы данных для корректной связки объектов
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
