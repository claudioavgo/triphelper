from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
    
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
        else:
            usr = None

        return f(request, user=usr, *args, **kwargs)
    return funcao_decorada

@requer_autenticacao
def index(request, user):
    print(user)
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
def destination(request, country_iso, city, user):
    context = {
        "content": touristAttractions(city, country_iso), 
        "country": getCountryByIso(country_iso), 
        "city": city, 
        "iso": str(country_iso).lower(),
        "plug": plugType(country_iso),
        "info": countryInformations(country_iso),
        "user": user
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



   
    
