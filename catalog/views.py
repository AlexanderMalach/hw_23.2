from django.shortcuts import render

from catalog.forms import ContactForm
from catalog.models import Product, ContactInfo
from django.shortcuts import render, redirect

def render_home(request):
    return render(request, 'home.html')


# def render_contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"Имя пользователя: {name}\nНомер телефона: {phone}\nСообщения от пользователя: {message}")
#     return render(request, 'contacts.html')


def render_contacts(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(product)
    return render(request, 'contacts.html', {'latest_products': latest_products})


# def contact_page(request):
#     contacts = ContactInfo.objects.all()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"Имя пользователя: {name}\nНомер телефона: {phone}\nСообщения от пользователя: {message}")
#     return render(request, 'contacts/contact_page.html', {'contacts': contacts})


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение данных в базу данных
            return redirect('contact_page')  # Перенаправление после сохранения
    else:
        form = ContactForm()

    contacts = ContactInfo.objects.all()
    return render(request, 'contacts/contact_page.html', {'form': form, 'contacts': contacts})