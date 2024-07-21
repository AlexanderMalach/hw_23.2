# в вашем приложении (например, contacts) в файле forms.py
from django import forms
from catalog.models import ContactInfo


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['name', 'phone', 'message']

