from django.contrib import admin

from catalog.models import Product, Category, ContactInfo


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "price",
    )
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "message",
    )

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish_date", 'views_counter')