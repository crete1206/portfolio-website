from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        # Save to database
        ContactMessage.objects.create(name=name, email=email, message=message_text)
        
        # Add a success message
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')

    return render(request, 'index.html')