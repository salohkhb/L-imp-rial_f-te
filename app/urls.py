from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact_us, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
        ]