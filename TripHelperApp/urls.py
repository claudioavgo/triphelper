from django.urls import path

from . import views

urlpatterns = [
    path("api/<str:country>/cities", views.retryCities, name="retryCities"),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
]