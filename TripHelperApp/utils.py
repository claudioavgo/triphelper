import json
import requests
from deep_translator import GoogleTranslator

apiKey = "5ae2e3f221c38a28845f05b6b4a3b5bf3698002c3857a171f8a470c1"

def countries():
    url = "https://countriesnow.space/api/v0.1/countries"
    req = requests.get(url)

    if req.status_code == 200:
        lista_paises = [] 
          
        dicionario_paises = json.loads(req.text)

        for i in range(228):
            lista_paises.append({"name": dicionario_paises["data"][i]["country"], "iso": dicionario_paises["data"][i]["iso2"]})
    
        return lista_paises
    
    else:
        return []
    
def cities(country_iso):
    url = "https://countriesnow.space/api/v0.1/countries"
    req = requests.get(url)

    if req.status_code == 200:
        cities_list = []
            
        dicionario_paises = json.loads(req.text)

        for i in range(228):
            if dicionario_paises["data"][i]["iso2"] == country_iso:
                cities_list = dicionario_paises["data"][i]["cities"]
        
        return cities_list
    
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
            i["properties"]["name"] = GoogleTranslator(source='auto', target='pt').translate(i["properties"]["name"])
            i["wikidata"] = getMorePlaceInfo(i["properties"]["wikidata"])
            try:
                texto = GoogleTranslator(source='auto', target='pt').translate(i["wikidata"]["wikipedia_extracts"]["text"])

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