from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education_view, name='education'),
    path('experience/', views.education_view, name='experience'),
    path('contact/', views.contact_view, name='contact'),
    path('manage_experience/', views.manage_experience, name='manage_experience'),
]
