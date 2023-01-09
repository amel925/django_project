import os
import requests
from pymongo import MongoClient

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo   
    CONNECTION_STRING = "mongodb+srv://linux_site_web:o0uh950JLuOCL8Ww@cluster0.3iix0gl.mongodb.net/test?retryWrites=true&w=majority"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient   
    client = MongoClient(CONNECTION_STRING)
    # Create the database for our example (we will use the same database throughout the tutorial   
    return client['test']

url="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=prod-nat-gaz-horaire-prov&q=&rows=9100&sort=-journee_gaziere&facet=journee_gaziere&facet=operateur&timezone=Europe%2FParis"
url2="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=eco2mix-metropoles-tr&q=&rows=9000&sort=-date&facet=libelle_metropole&timezone=Europe%2FParis"
url3="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=cccg-horaire-nat&q=&rows=9000&sort=jourcalendaire&facet=jourcalendaire&timezone=Europe%2FParis"
    

def collection_gaz(url):
    r=requests.get(url)

    velib=r.json()

    dbname = get_database()

    dbname.test_collection.delete_many({})
    dbname.test_collection.insert_many(velib['records'])

    
def collection_electricite(url):
    
    r=requests.get(url)

    velib=r.json()

    dbname = get_database()

    dbname.test_collection2.delete_many({})
    dbname.test_collection2.insert_many(velib['records'][ : : -1])

def collection_gazCombine(url):
    
    r=requests.get(url)

    velib=r.json()

    dbname = get_database()

    dbname.test_collection3.delete_many({})
    dbname.test_collection3.insert_many(velib['records'][ : : -1])

collection_gaz(url)
collection_electricite(url2)
collection_gazCombine(url3)