from django.shortcuts import render


def render_home(request):
    return render(request, 'home.html')


def render_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя пользователя: {name}\nНомер телефона: {phone}\nСообщения от пользователя: {message}")
    return render(request, 'contact.html')
