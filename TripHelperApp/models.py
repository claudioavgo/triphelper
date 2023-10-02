from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager

# Create your models here.    

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    credits = models.IntegerField()

    def check_account(username, password):
        if User.objects.get(username=username, password=password):
            return True