from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name='index'),
    path("about/", views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('services/', views.Service, name='services'),
    path('service/<slug:slug>', views.Service_Detail, name='service_detail'),
]
