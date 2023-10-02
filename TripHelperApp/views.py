from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

# from django.contrib.auth.models import User

from .models import *

from .utils import *

# Create your views here.

# Home Page
def index(request):
    countries_list = countries()

    cities_list = []
    
    while cities_list == []:
        random_country = random.choice(countries_list)
        cities_list = cities(random_country['iso'])
    
    logged = False

    context = {
        'countries_list': countries_list,
        'random_country': random_country,
        'random_city': random.choice(cities_list),
        'account': logged
    }

    return render(request, 'index.html', context)

#Cities API
def retryCities(request, country):
    cities_list = cities(country)

    context = {'cities': cities_list}

    return JsonResponse(context)

# About Page
def about(request):
    return render(request, 'about.html')

# Top Page
def top(request):
    return render(request, 'top.html')

# Destination Page
def destination(request, country_iso, city):
    context = {
        "content": touristAttractions(city, country_iso), 
        "country": getCountryByIso(country_iso), 
        "city": city, 
        "iso": str(country_iso).lower(),
        "plug": plugType(country_iso),
        "info": countryInformations(country_iso)
    }

    return render(request, 'destination.html', context)

def register(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST["email"], password=request.POST["password"])
            return redirect("/top")
        except:
            return redirect("/register?error=1")
    else:
        context = {"error": request.GET.get("error", 0)}
        return render(request, 'register.html', context)



   
    
