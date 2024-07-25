from django.shortcuts import render, redirect, get_object_or_404

from catalog.forms import ContactForm
from catalog.models import Product, ContactInfo


def render_home(request):
    return render(request, 'home.html')


def render_contacts(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(product)
    return render(request, 'contacts.html', {'latest_products': latest_products})


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


# def render_base(request):
#     return render(request, 'base.html')


def render_base(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)


def product_ditail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context1 = {'product': product}
    return render(request, 'product_ditail.html', context1)