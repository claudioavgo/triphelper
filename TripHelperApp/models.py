from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class FavoritePlace(models.Model):
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    iso2 = models.CharField(max_length=2, default=None, blank=None)

    def __str__(self):
        return self.city
class Comment(models.Model):
    text = models.TextField()
    likes = models.IntegerField(default=0)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)

    def like(self):
        self.likes += 1
        self.save()

    def dislike(self):
        self.likes -= 1
        self.save()
    
    def __str__(self):
        return self.text
    
class Place(models.Model):
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    comments = models.ManyToManyField(Comment, default=None, blank=True)

    def __str__(self):
        return self.city

class Perfil(models.Model):
    credits = models.IntegerField(default=10)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)
    favPlaces = models.ManyToManyField(FavoritePlace, default=None, blank=True)

    def getFavPlaces(self):
        
        return [y.city for y in self.favPlaces.all()]

    def __str__(self):
        return self.usuario.username
    
