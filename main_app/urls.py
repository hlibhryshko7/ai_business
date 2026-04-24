from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('reviews/', views.reviews, name='reviews'),
    path('training/', views.training, name='training'),
    path('contact/', views.contact, name='contact'),
]