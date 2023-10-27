from django.db import models
from django.contrib.auth.models import User

# Create your models here.    

class Perfil(models.Model):
    credits = models.IntegerField(default=10)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username