from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import OperationalError
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not name or not email or not message_text:
            messages.error(request, 'Please fill in your name, email, and message before sending.')
            return redirect('home')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Please enter a valid email address.')
            return redirect('home')

        try:
            ContactMessage.objects.create(name=name, email=email, message=message_text)
        except OperationalError:
            messages.error(request, 'Your message could not be saved right now. Please email me directly at alameenbusari70@gmail.com.')
            return redirect('home')

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')

    return render(request, 'index.html')
