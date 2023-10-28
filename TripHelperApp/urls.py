from django.urls import path

from . import views

urlpatterns = [
    path("api/<str:country>/cities", views.retryCities, name="retryCities"),
    path("destination/<str:country_iso>/<str:city>", views.destination, name="destination"),
    path("register", views.registerPage, name="register"),
    path("logout", views.logoutPage, name="logoutPage"),
    path("login", views.loginPage, name="login"),
    path("about", views.about, name="about"),
    path("top", views.top, name="top"),
    path("", views.index, name="index"),
    path('like/', views.like_view, name='like'),
    path('dislike/', views.dislike_view, name='dislike'),
]