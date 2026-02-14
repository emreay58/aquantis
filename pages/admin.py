from django.contrib import admin
from .models import FormModel, Carousel, ServiceModel

@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

# Register your models here.
admin.site.register(Carousel)
admin.site.register(FormModel)