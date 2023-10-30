from django.urls import path

from . import views

urlpatterns = [
    path("api/<str:country>/cities", views.retryCities, name="retryCities"),
    path("api/feed", views.likeControlAPI, name="likeControlAPI"),
    path("destination/<str:country_iso>/<str:city>", views.destination, name="destination"),
    path('account/', views.account, name='account'),
    path("register", views.registerPage, name="register"),
    path("logout", views.logoutPage, name="logoutPage"),
    path("login", views.loginPage, name="login"),
    path("about", views.about, name="about"),
    path("top", views.top, name="top"),
    path("", views.index, name="index"),
]