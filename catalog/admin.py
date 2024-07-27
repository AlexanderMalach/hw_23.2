from django.contrib import admin

from catalog.models import Product, Category, ContactInfo, Blog


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


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", 'content', "date_creation", 'publication_sign')