import os
import requests
#Client for a MongoDB instance.
#allows to establish a connection between their Python application and MongoDB to manage data
#  in a Database.
from pymongo import MongoClient

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo   
    CONNECTION_STRING = "mongodb+srv://linux_site_web:o0uh950JLuOCL8Ww@cluster0.3iix0gl.mongodb.net/test?retryWrites=true&w=majority"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient   
    client = MongoClient(CONNECTION_STRING)
    # Create the database for our example (we will use the same database throughout the tutorial   
    return client['test']


# Production horaire provisoire de biométhane des sites d'injection raccordés au réseau de transport de gaz en France
url="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=prod-nat-gaz-horaire-prov&q=&rows=9100&sort=-journee_gaziere&facet=journee_gaziere&facet=operateur&timezone=Europe%2FParis"
# Consommation d'électricité des grandes Métropoles françaises temps réel
url2="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=eco2mix-metropoles-tr&q=&rows=10000&sort=-date&facet=libelle_metropole&timezone=Europe%2FParis"
# Consommation quotidienne de gaz des Centrales à Cycle Combiné Gaz (zone GRTgaz)
url3="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=cccg-horaire-nat&q=&rows=9000&sort=jourcalendaire&facet=jourcalendaire&timezone=Europe%2FParis"
    

""" 
fonction qui recupere les données depuis l'api du gaz.
la recuperation s'effectue dans le sens inverses afin d'obtenir les données de la plus ancienne à la plus recente  ( ceci est fait lors de la definition de l'url de l'api)
parametre: url de l'api

"""
def collection_gaz(url):
    r=requests.get(url)

    velib=r.json()

    dbname = get_database()

    dbname.test_collection.delete_many({})
    dbname.test_collection.insert_many(velib['records'])



""" 
fonction qui recupere les données depuis l'api de l'electricité .
la recuperation s'effectue dans le sens inverses afin d'obtenir les données de la plus recente à la plus ancienne ( ceci est fait lors de la definition de l'url de l'api) qui ensuite ont été remises dont l'ordre inverse pour le bon fonctionnement du code
parametre: url de l'api

"""
def collection_electricite(url):
    
    r=requests.get(url)

    velib=r.json()

    dbname = get_database()

    dbname.test_collection2.delete_many({})

    
    dbname.test_collection2.insert_many(velib['records'][ : : -1])



""" 
fonction qui recupere les données depuis l'api du gaz combiné.
dans la fonction les données ont été ordonnées dans le sens inverse afin d'avoir des plus anciennes au plus recentes.
parametre: url de l'api

"""

def collection_gazCombine(url):
    
    r=requests.get(url)

    velib=r.json()

    dbname = get_database()

    dbname.test_collection3.delete_many({})
    dbname.test_collection3.insert_many(velib['records'][ : : -1])

collection_gaz(url)
collection_electricite(url2)
collection_gazCombine(url3)