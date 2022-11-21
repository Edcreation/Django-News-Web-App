import email
from unicodedata import name
from django.db import models

# Create your models here.

class Newsfeed(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    details = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.title} - {self.slug}'

class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    