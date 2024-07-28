from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание продукта",
    )
    photo = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите название категории",
        blank=True,
        null=True,
        related_name="products",
    )

    price = models.IntegerField(
        verbose_name="Цена за покупку",
        help_text="Введите цену продукта",
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Счётчик просмотров",
        help_text="Укажите количество просмотров",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    # в вашем приложении (например, contacts) в файле models.py


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
    )
    content = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    date_creation = models.DateTimeField(verbose_name="Дата создания")
    publication_sign = models.BooleanField(verbose_name="Опубликовано?", default=False)
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Счётчик просмотров",
        help_text="Укажите количество просмотров",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("catalog:blog_detail", kwargs={"pk": self.pk, "slug": self.slug})

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["publication_sign", "-date_creation"]


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
    )
    version_number = models.PositiveIntegerField(
        verbose_name="Номер версии",
        help_text="Введите номер версии",
    )
    version_name = models.CharField(
        verbose_name="Название версии",
        help_text="Введите название версии",
        blank=True,
        null=True,
    )
    indication_current_version = models.BooleanField(
        verbose_name="Признак текущей версии.",
        help_text="Введите признак текущей версии",
        default=False
    )

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = ["indication_current_version", 'version_number']