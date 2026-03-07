from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class ServiceModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Hizmet Adı')
    description = models.TextField(verbose_name='Hizmet Açıklaması')
    description_big = RichTextField(verbose_name="Geniş Açıklama ve Yazı")
    image = CloudinaryField('image')
    slug= models.SlugField()
    is_active =models.BooleanField(verbose_name='Hizmet Aktif Mi')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/service/{self.slug}/'

class Carousel(models.Model):
    caption1 = models.CharField(max_length=100, verbose_name='Altyazı1')
    caption2 = models.CharField(max_length=200, verbose_name='Altyazı2')
    link = models.CharField(max_length=100)
    image = CloudinaryField('image', help_text="Ölçü: 1920x570")
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')

    def __str__(self):
        return "{} - {}".format(self.caption1, self.caption2)


class FormModel(models.Model):
    message = models.TextField(verbose_name='Mesaj')
    name = models.CharField(max_length=100, verbose_name='İsim Soyisim')
    telefon = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    