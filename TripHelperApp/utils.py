import json
import requests

apiKey = "5ae2e3f221c38a28845f05b6b4a3b5bf3698002c3857a171f8a470c1"

def countries():
    url = "https://countriesnow.space/api/v0.1/countries"
    req = requests.get(url)

    if req.status_code == 200:
        lista_paises = []
        
        dicionario_paises = json.loads(req.text)

        for i in range(228):
            lista_paises.append(dicionario_paises["data"][i]["country"])
    
        return lista_paises
    
    else:
        return "Lista vazia"
    
def cities(country):
    url = "https://countriesnow.space/api/v0.1/countries"
    req = requests.get(url)

    if req.status_code == 200:
        cities_list = []
            
        dicionario_paises = json.loads(req.text)

        for i in range(228):
            if dicionario_paises["data"][i]["country"] == country:
                cities_list = dicionario_paises["data"][i]["cities"]
        
        return cities_list
    
def findCoordinates(city, country):
    url = f"https://api.opentripmap.com/0.1/en/places/geoname?name={city}&country={country}&apikey={apiKey}"

    req = requests.get(url)

    if req.status_code == 200:
        return json.loads(req.text)
    else:
        return []
    
def touristAttractions(lon, lat):
    url = f"https://api.opentripmap.com/0.1/en/places/radius?radius=10000&lon={lon}&lat={lat}&src_geom=wikidata&src_attr=wikidata&apikey={apiKey}"

    req  = requests.get(url)

    if req.status_code == 200:
        return json.loads(req.text)
    else:
        return []