from django.db import models

class Merch(models.Model):
    name = models.TextField()
    item = models.TextField(blank=True)
    price = models.TextField(blank=True)
    stock = models.BooleanField()
    url = models.TextField()
    merch_id = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='merch', on_delete=models.CASCADE)

class Release(models.Model):
    name = models.TextField()
    artist = models.TextField()
    url = models.TextField()
    embed = models.TextField()
    release_number = models.TextField(blank=True)
    medium = models.TextField(blank=True)
    release_id = models.TextField()
    description = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='releases', on_delete=models.CASCADE)

class Video(models.Model):
    name = models.TextField()
    artist = models.TextField()
    embed = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='videos', on_delete=models.CASCADE)

# Create your models here.
