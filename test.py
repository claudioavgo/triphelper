import requests
import json

url = "https://countriesnow.space/api/v0.1/countries"
req = requests.get(url)

if req.status_code == 200:
    cities_list = []
        
    dicionario_paises = json.loads(req.text)

    for i in range(228):
        if dicionario_paises["data"][i]["country"] == "Brazil":
            cities_list = dicionario_paises["data"][i]["cities"]