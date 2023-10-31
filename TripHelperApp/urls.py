from django.urls import path

from . import views

urlpatterns = [
    path("destination/<str:country_iso>/<str:city>", views.destination, name="destination"),
    path("api/<str:country>/cities", views.retryCities, name="retryCities"),
    path("api/feed", views.likeControlAPI, name="likeControlAPI"),
    path("register", views.registerPage, name="register"),
    path("api/comment", views.commentAPI, name='account'),
    path("logout", views.logoutPage, name="logoutPage"),
    path("login", views.loginPage, name="login"),
    path("about", views.about, name="about"),
    path("", views.index, name="index"),
    path("top", views.top, name="top"),
    path("account/", views.account, name="account")
]