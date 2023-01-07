import os
import requests

def velib():
    url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&timezone=Europe%2FParis"

    r = requests.get(url)
    droplets = r.json()
    #droplet_list = []

    #for i in range(len(droplets['droplets'])):
    #    droplet_list.append(droplets['droplets'][i])
    return droplets