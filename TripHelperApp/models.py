from django.db import models
from django.contrib.auth.models import User

# Create your models here.    

class Perfil(models.Model):
    credits = models.IntegerField(default=10)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title 
    
    def increase_likes(self):
        self.likes += 1
        self.save()