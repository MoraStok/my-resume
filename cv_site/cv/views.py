from django.shortcuts import render, redirect
from .models import Experience, Education
from .forms import ContactForm

def home(request):
    return render(request, 'cv/home.html')

def education_view(request):
    education = Education.objects.all()
    return render(request, 'cv/education.html', {'education': education})

def experience_view(request):
    experience = Experience.objects.all()
    return render(request, 'cv/experience.html', {'experience': experience})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'cv/contact.html', {'form': form})