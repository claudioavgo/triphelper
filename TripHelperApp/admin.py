from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Perfil)
admin.site.register(Comment)
admin.site.register(Place)
admin.site.register(FavoritePlace)