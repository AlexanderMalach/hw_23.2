# Generated by Django 4.2.2 on 2024-07-31 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Country"
            ),
        ),
    ]
