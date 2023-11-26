from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import *
from .utils import *

# Create your views here.

# Home Page

def requer_autenticacao(f):
    def funcao_decorada(request, *args, **kwargs):
        # Verifica session['logado']
        if (request.user.is_authenticated):
            username = request.user

            usr = Perfil.objects.get(usuario=User.objects.get(username=username))
            usr.getFavPlaces
        else:
            usr = None

        return f(request, user=usr, *args, **kwargs)
    return funcao_decorada

@requer_autenticacao
def index(request, user):
    countries_list = countries()

    cities_list = []
    
    while cities_list == []:
        random_country = random.choice(countries_list)
        cities_list = cities(random_country['iso'])

    context = {
        'countries_list': countries_list,
        'random_country': random_country,
        'random_city': random.choice(cities_list),
        'user': user,
    }

    return render(request, 'index.html', context)

#Cities API
def retryCities(request, country):
    cities_list = cities(country)

    context = {'cities': cities_list}

    return JsonResponse(context)

# About Page
@requer_autenticacao
def about(request, user):
    context = {
        'user': user,
    }
    return render(request, 'about.html', context)

# Top Page
@requer_autenticacao
def top(request, user):
    context = {
        'user': user,
    }
    return render(request, 'top.html', context)

# Destination Page
@requer_autenticacao
#@cache_page(60 * 60)
def destination(request, country_iso, city, user):

    country_ = getCountryByIso(country_iso)

    try:
        place = Place.objects.get(city=city)
    except:
        place = Place.objects.create(city=city, country=country_)

    if country_iso == "TS" and city == "Teste":
        context = {
            "content": False, 
            "country": False, 
            "city": city, 
            "iso": str(country_iso).lower(),
            "plug": [],
            "info": False,
            "user": user
        }
    else:
        context = {
            "content": touristAttractions(city, country_iso),
            "country": country_, 
            "city": city,
            "iso": str(country_iso).lower(),
            "plug": plugType(country_iso),
            "info": countryInformations(country_iso),
            "user": user,
            "favPlaces": user.getFavPlaces if user else [],
            "comments": place.comments.all()
        }

    return render(request, 'destination.html', context)

def registerPage(request):
    if request.method == "POST":
            e = User.objects.filter(email=request.POST.get("email")).count()
            if e == 0:
                try:
                    user = User.objects.create_user(email=request.POST.get("email"), username=request.POST.get("username"), password=request.POST.get("password"))
                    Perfil.objects.create(usuario=user, credits=10)
                    login(request, user)
                    send_mail_message("teste", request.POST.get("email"))
                except:
                    print("Email já cadastrado")
                    return redirect("/register?error=1")
            else:
                print("Email já cadastrado")
                return redirect("/register?error=1")
        
            return redirect("/")
    else:
        context = {"error": request.GET.get("error", 0)}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.method == "POST":
        try:
            username = User.objects.get(email=request.POST.get("email")).username
            user = authenticate(request, username=username, password=request.POST.get("password"))

            if (user):
                login(request, user)
        
            return redirect("/")
        except:
            return redirect("/login?error=1")
    else:
        context = {"error": request.GET.get("error", 0)}
        return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect("/")

@requer_autenticacao
def account(request, user):
    context = {
        'user': user,
        'fav': Perfil.objects.get(usuario=user.usuario).favPlaces.all()
    }
    return render(request, 'logged/dashboard.html', context=context)

@requer_autenticacao
def likeControlAPI(request, user):
    
    country = request.GET['country']
    city = request.GET['city']
    iso2 = request.GET['iso2']
    type = request.GET['type']

    real_user = Perfil.objects.get(usuario=user.usuario)

    if str(type).lower() == "like":

        try:
            fp = FavouritePlace.objects.get(city=city)
        except:
            fp = FavouritePlace.objects.create(city=city, country=country, iso2=iso2)

        real_user.favPlaces.add(fp)

    else:
        fp = FavouritePlace.objects.get(city=city)
        real_user.favPlaces.remove(fp)
        
    context = {'city': city, 'country': country, 'iso2': iso2, 'type': type}

    return JsonResponse(context)


@requer_autenticacao
def commentAPI(request, user):
    
    country = request.GET['country']
    city = request.GET['city']
    comment = request.GET['comment']

    print(user)

    real_user = Perfil.objects.get(usuario=user.usuario)

    if comment:
        cmmt = Comment.objects.create(text=comment, author=user.usuario)

        try:
            p = Place.objects.get(country=country, city=city)
        except:
            p = Place.objects.create(country=country, city=city)
        
        p.comments.add(cmmt)

    context = {}

    return JsonResponse(context)

@requer_autenticacao
def intro_game(request, user):
    context = {
        'user': user,
    }
    return render(request, 'intro_game.html', context=context)

@requer_autenticacao
def game(request, user):
    context = {
        'user': user,
    }
    return render(request, 'game.html', context=context)