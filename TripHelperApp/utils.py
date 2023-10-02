import os
import json
import random
import requests
from dotenv import load_dotenv
from deep_translator import GoogleTranslator

load_dotenv()

apiKey = "5ae2e3f221c38a28845f05b6b4a3b5bf3698002c3857a171f8a470c1"

def countries():
    try:
        with open('./TripHelperApp/static/bin/countries.json', 'r', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
        
        lista_paises = []
          
        dicionario_paises = data

        for i in range(228):
            lista_paises.append({"name": dicionario_paises["data"][i]["country"], "iso": dicionario_paises["data"][i]["iso2"]})
    
        return lista_paises
    except:
        return []
    
def cities(country_iso):
    try:
        with open('./TripHelperApp/static/bin/countries.json', 'r', encoding='utf-8') as json_file:
            data = json.loads(json_file.read())
        
        cities_list = []
          
        dicionario_paises = data

        for i in range(228):
            if dicionario_paises["data"][i]["iso2"] == country_iso:
                cities_list = dicionario_paises["data"][i]["cities"]
    
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
    
def touristAttractions(city, country):
    coordinates = findCoordinates(city, country)

    print(coordinates)

    lon = coordinates["lon"]
    lat = coordinates["lat"]

    url = f"https://api.opentripmap.com/0.1/en/places/radius?radius=10000&lon={lon}&lat={lat}&src_geom=wikidata&src_attr=wikidata&limit=6&apikey={apiKey}"
    
    req  = requests.get(url)
    
    attractions = json.loads(req.text)

    if req.status_code == 200:

        for i in attractions["features"]:
            i["properties"]["googleName"] = i["properties"]["name"]
            i["properties"]["name"] = GoogleTranslator(source='auto', target='en').translate(i["properties"]["name"])
            i["wikidata"] = getMorePlaceInfo(i["properties"]["wikidata"])
            try:
                texto = GoogleTranslator(source='auto', target='en').translate(i["wikidata"]["wikipedia_extracts"]["text"])

                if len(texto) > 232:
                    i["wikidata"]["wikipedia_extracts"]["text"] = texto[:232]+"..."
            except:
                print("Não possui")
            
            try:
                i["wikidata"]["preview"]["source"] = i["wikidata"]["preview"]["source"]
            except:
                i["wikidata"]["preview"] = {'source': 'https://htmlcolorcodes.com/assets/images/colors/white-color-solid-background-1920x1080.png'}
        
        #print(attractions)

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
    url = "https://countriesnow.space/api/v0.1/countries"
    req = requests.get(url)

    if req.status_code == 200:
        country = ""
          
        dicionario_paises = json.loads(req.text)

        for i in range(228):
            if dicionario_paises["data"][i]["iso2"] == iso:
                country = dicionario_paises["data"][i]["country"]
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