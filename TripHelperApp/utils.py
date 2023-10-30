import os
import json
import random
import resend
import requests
from dotenv import load_dotenv
from django.conf import settings
import schedule
from django.core.mail import send_mail
from deep_translator import GoogleTranslator
from django.core.cache import cache

load_dotenv()

resend.api_key = "re_fcxxQ6Sw_87NSeQksyKyXouMsyR8YVUzE"
apiKey = "5ae2e3f221c38a28845f05b6b4a3b5bf3698002c3857a171f8a470c1"



def countries():
    try:
        with open('./TripHelperApp/static/bin/countries.json', 'r', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
        
        lista_paises = []
          
        dicionario_paises = data

        for i in dicionario_paises["data"]:
            lista_paises.append({"name": i["country"], "iso": i["iso2"]})
    
        return lista_paises
    except:
        return []
    
def cities(country_iso):
    try:
        with open('./TripHelperApp/static/bin/countries.json', 'r', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
        
        cities_list = []
          
        dicionario_paises = data

        for i in dicionario_paises["data"]:
            if i["iso2"] == country_iso:
                cities_list = i["cities"]
    
        return cities_list
    except Exception as e:
        print(e)
        return []
    
def findCoordinates(city, country):
    url = f"https://api.opentripmap.com/0.1/en/places/geoname?name={city}&country={country}&apikey={apiKey}"

    req = requests.get(url)

    if req.status_code == 200:
        return json.loads(req.text)
    else:
        return []
    
# def touristAttractions(city, country):
    
#     with open('./TripHelperApp/static/bin/cache.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
    

#     try:
#         if data[city]:
#             return data[city]
#     except:
#         url = f"https://places-api-5dim.onrender.com/places?city={city}&country={country}"
        
#         req  = requests.get(url)
        
#         attractions = json.loads(req.text)

#         if req.status_code == 200:

#             data[city] = attractions

#             with open('./TripHelperApp/static/bin/cache.json', 'w', encoding='utf-8') as file:
#                 file.write(json.dumps(data, indent=4))

#             return attractions
#         else:
#             return []
        
def touristAttractions(city, country):
    
    ch = cache.get(city)

    if ch:
        print("cached")
        return ch
    else:
        url = f"https://places-api-5dim.onrender.com/places?city={city}&country={country}"
        
        req  = requests.get(url)
        
        attractions = json.loads(req.text)

        if req.status_code == 200:

            cache.set(city, attractions, None)

            return attractions
        else:
            return []

def getMorePlaceInfo(xid):
    url_info = f"https://api.opentripmap.com/0.1/en/places/xid/{xid}?apikey={apiKey}"

    req = requests.get(url_info)

    if req.status_code == 200:

        return json.loads(req.text)
    
    else:
        return []

def getCountryByIso(iso):
    with open('./TripHelperApp/static/bin/countries.json', 'r', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())

    if data:
        country = ""
          
        dicionario_paises = data

        for i in dicionario_paises["data"]:
            if i["iso2"] == iso:
                country = i["country"]
        return country
    
    else:
        return ""
    
def randomdestination():

    country_list = countries()
    
    selected_country = random.choice(country_list)
    country_iso = selected_country["iso"]

    city_list = cities(country_iso)

    if not city_list:
        return selected_country["iso"], None
    
    selected_city = random.choice(city_list)

    return selected_country["iso"], selected_city

def plugType(iso2):
    api_url = "https://raw.githubusercontent.com/claudioavgo/triphelper/main/TripHelperApp/static/bin/plug.csv"
    data = requests.get(api_url)
    types = []

    for i in data.text.split("\n"):
        if iso2 in i:
            types.append(i.split(",")[4])
    return types

def countryInformations(iso2):
    countryName = getCountryByIso(iso2)
    api_url = f"https://restcountries.com/v3.1/name/{countryName}"
    data = json.loads(requests.get(api_url).text)
    languages = []

    for i in data[0]["languages"]:
        languages.append(data[0]["languages"][i])
    
    data[0]["languages"] = languages
    
    return data


def iso3toiso2(iso3: str) -> str:
    try:
        with open('./TripHelperApp/static/bin/countries.json', 'r', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
        
        iso2 = None

        for i in data["data"]:
            if i["iso3"] == iso3:
                return i["iso2"]
    except:
        return None

def send_mail_message(message, to): 
    params = {
    "from": "TripHelperCompany <TripHelper@claudioav.com>",
    "to": [to],
    "subject": "👋 Hello from TripHelper!",
    "html": f"""
        <h1>{message}</h1> 
    """,
    }

    email = resend.Emails.send(params)
    print(email)

def test_cache():
    #cache.set('mykey', 'myvalue')

    print(cache.get('mykey'))