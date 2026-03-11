from django.shortcuts import render
from .models import ServiceModel, Carousel
from django.views.generic import TemplateView



def Index(request):
    service = ServiceModel.objects.all().order_by('id')
    carousel = Carousel.objects.all().order_by('id')

    context = {
        'service' : service,
        'carousel' : carousel
    }

    return render(request, 'pages/index.html', context)

def About(request):
    return render(request, "pages/about.html")

def Contact(request):
    return render(request, "pages/contact.html")

def Service(request):
    service = ServiceModel.objects.all().order_by('id')

    context = {
        'service' : service
    }
    return render (request, 'pages/services.html', context)


def Service_Detail(request, slug):
    service = ServiceModel.objects.get(slug=slug)

    context = {
        'service' : service
    }

    return render(request, "pages/service_detail.html", context) 


def error_404_view(request, exception):
    return render(request, 'pages/404.html')
