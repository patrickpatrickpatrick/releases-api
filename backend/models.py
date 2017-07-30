from django.db import models

class Merch(models.Model):
    name = models.TextField()
    item = models.TextField()
    price = models.TextField()
    stock = models.BooleanField()
    url = models.TextField()

class Release(models.Model):
    name = models.TextField()
    artist = models.TextField()
    url = models.TextField()
    embed = models.TextField()
    release_number = models.TextField(blank=True)
    medium = models.TextField(blank=True)
    release_id = models.TextField()
    description = models.TextField(blank=True)

class Video(models.Model):
    name = models.TextField()
    artist = models.TextField()
    embed = models.TextField()

# Create your models here.
