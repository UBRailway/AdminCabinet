from django.http import HttpResponse
from django.shortcuts import render

def admincab(request):
    context= {
    'name_lil': 'Bair G.',
    'name': 'Bair',
    'second_name': 'Gandbolt',
    'job': 'Admin',
    'area': 'Trans-Mongolian Highway',
    'station': 'Ulanbaatar-1',
    'phone_number': '+99754298',
    'mail': 'nowera_yoku84@yahoo.com'
    }
    return render(request,'main/admincab_main.html',context)
    
def users(request):
    return HttpResponse('users page')
