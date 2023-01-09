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


def velib():
    url2="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=prod-nat-gaz-horaire-prov&q=&rows=9100&sort=-journee_gaziere&facet=journee_gaziere&facet=operateur&timezone=Europe%2FParis"
    r=requests.get(url2)

    velib=r.json()

    dbname = get_database()

    dbname.test_collection.delete_many({})
    dbname.test_collection.insert_many(velib['records'])
    data=dbname.test_collection.find()