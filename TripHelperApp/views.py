from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .utils import *

# Create your views here.

# Home Page
def index(request):
    countries_list = countries()

    context = {'countries_list': countries_list}

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
    
    context = {"content": touristAttractions(city, country_iso), "country": getCountryByIso(country_iso), "city": city, "iso": str(country_iso).lower()}

    return render(request, 'destination.html', context)

def random_Destination(request):
    selected_country, selected_city = randomdestination()

    if selected_country and selected_city:

         return redirect('destination', country=selected_country, city=selected_city)
    else:
    
        return render(request, 'error.html', {'message': 'Não foi possível obter um destino aleatório.'})