import json

import requests


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