from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context= {
    'name': 'Баир',
    'job': 'Админ',
    'area': 'Восточно-Сибирская ж.д',
    'station': 'Иркутск-Пассажирский',
    'phone_number': '+7(950)073 3180',
    'mail': 'Znaidyuk00@gmail.com'
    }
    return render(request,'main/index.html',context)


def users(request):
    return render(request,'main/users.html')