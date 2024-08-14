# Generated by Django 4.2.2 on 2024-08-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0017_product_publication_sign"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="publication_sign",
            field=models.BooleanField(
                default=False, help_text="Whether", verbose_name="Опубликовано?"
            ),
        ),
    ]