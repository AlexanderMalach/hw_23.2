# Generated by Django 5.0.7 on 2024-07-20 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_contactinfo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contactinfo",
            old_name="address",
            new_name="message",
        ),
    ]