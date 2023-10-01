from django.urls import path

from . import views

urlpatterns = [
    path("api/<str:country>/cities", views.retryCities, name="retryCities"),
    path("destination/<str:country_iso>/<str:city>", views.destination, name="destination"),
    path('randomdestination/', views.random_Destination, name='randomdestination'),
    path("about", views.about, name="about"),
    path("top", views.top, name="top"),
    path("", views.index, name="index"),
]