from django.shortcuts import render, redirect
from .models import Experience, Education, WorkExperience
from .forms import ContactForm, WorkExperienceForm

def home(request):
    return render(request, 'base.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'cv/contact.html', {'form': form})

def manage_experience(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_experience')
    else:
        form = WorkExperienceForm()
    
    experiences = WorkExperience.objects.all()
    return render(request, 'cv/manage_experience.html', {'form': form, 'experiences': experiences})
