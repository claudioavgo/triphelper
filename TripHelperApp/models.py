from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FavouritePlace(models.Model):
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    iso2 = models.CharField(max_length=2, default=None, blank=None)

    def __str__(self):
        return self.city
class Comment(models.Model):
    text = models.TextField()
    likes = models.IntegerField(default=0)
    author = models.CharField(default="Nenhum", null=True, blank=True)
    id =  models.AutoField(primary_key=True)

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
    comments = models.ManyToManyField(Comment, default=None, blank=True)
    favPlaces = models.ManyToManyField(FavouritePlace, default=None, blank=True)

    def getFavPlaces(self):
        lista_de_cidades_com_like = [y.city for y in self.favPlaces.all()]
        print(lista_de_cidades_com_like)
        return lista_de_cidades_com_like

    def __str__(self):
        return self.usuario.username
    
