# в вашем приложении (например, contacts) в файле forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = ["form-check-input"]
            else:
                field.widget.attrs["class"] = ["form-control"]


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["views_counter", "owner"]

    def clean_name(self):
        cleaned_data = self.cleaned_data.get("name")
        ban_list_name = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for ban_name in ban_list_name:
            if ban_name == cleaned_data:
                raise ValidationError("Имя не должно содержать запрещенные слова")
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
