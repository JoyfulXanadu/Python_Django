from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Здесь стоит обработать данные, например, сохранить их в базу данных
        # или отправить по электронной почте

        # После обработки данных перенаправляем пользователя на другую страницу
        # использую reverse, чтобы генерировать URL по имени маршрута
        return HttpResponseRedirect(
            reverse('home'))  # Перенаправляем на домашнюю страницу сайта

    return render(request, 'catalog/contacts.html')


def products(request):
    return render(request, 'catalog/products.html')