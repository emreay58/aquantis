from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import ServiceModel


class PagesSitemap(Sitemap):
    def items(self):
        return ['index', 'about', 'contact',]

    def location(self, item):
        return reverse(item)

class ServicesSitemap(Sitemap):
    def items(self):
        return ServiceModel.objects.all()