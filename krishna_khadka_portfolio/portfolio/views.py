from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        'page_title': 'Krishna Khadka Portfolio',
        'welcome_message': 'Hello, welcome to my portfolio!',
    }
    return render(request, 'portfolio/home.html', context)