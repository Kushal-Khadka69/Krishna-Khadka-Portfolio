from django.shortcuts import render
from . import models
from django.contrib import messages
import re

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('content')
        number = request.POST.get('phone')

        # Name validation: letters and spaces only, 2-30 characters
        if not (2 <= len(name) <= 30) or not re.match(r'^[A-Za-z\s]+$', name):
            messages.error(request, "Name must be 2-30 characters and contain only letters.")
            return render(request, 'portfolio/home.html')

        # Email validation: proper email format
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            messages.error(request, "Please enter a valid email address.")
            return render(request, 'portfolio/home.html')

        # Phone validation: digits only (optionally starting with +), 7-15 digits
        if not re.match(r'^\+?\d{7,15}$', number):
            messages.error(request, "Phone number must contain only digits (7-15 digits, optional + prefix).")
            return render(request, 'portfolio/home.html')

        # Message validation: not empty
        if not message or len(message.strip()) < 1:
            messages.error(request, "Message cannot be empty.")
            return render(request, 'portfolio/home.html')

        ins = models.Contact(name=name, email=email, message=message, number=number)
        ins.save()
        messages.success(request, "Your message has been sent successfully. Thank you for contacting me.")

    return render(request, 'portfolio/home.html')