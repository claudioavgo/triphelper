from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .utils import *

# Create your views here.

#Homepage
def index(request):
    countries_list = countries()

    context = {'countries_list': countries_list}

    return render(request, 'index.html', context)

def retryCities(request, country):
    cities_list = cities(country)

    context = {'cities': cities_list}

    return JsonResponse(context)