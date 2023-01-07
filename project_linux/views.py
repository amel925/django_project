# connect to mongodb
import json
from django.http import HttpResponse
from pymongo import MongoClient
import requests
from django.shortcuts import render

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo   
    CONNECTION_STRING = "mongodb+srv://linux_site_web:o0uh950JLuOCL8Ww@cluster0.3iix0gl.mongodb.net/test?retryWrites=true&w=majority"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient   
    client = MongoClient(CONNECTION_STRING)
    # Create the database for our example (we will use the same database throughout the tutorial   
    return client['test']

def index(request):
    url="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=prod-nat-gaz-horaire-prov&q=&rows=10000&sort=journee_gaziere&timezone=Europe%2FParis"
    url2="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=prod-nat-gaz-horaire-prov"
    r=requests.get(url2)
    #r=requests.get('https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1000&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&facet=coverflow&facet=creditcard&facet=overflowactivation&facet=kioskstate&facet=station_state')
    velib=r.json()

    #print(velib)
    dbname = get_database()

    dbname.test_collection.delete_many({})
    dbname.test_collection.insert_many(velib['records'])
    data=dbname.test_collection.find()
    data1=[[d["fields"]["prod_journaliere_mwh_pcs"] for d in data]]
   
    print(data1)
    #return HttpResponse("Hello, world. You're at the index.")
    context={
        'data':data1,
    }
    print("ici ",context)
    return render(request, 'dashboard/index.html',context)


def index2(request):
    url2="https://odre.opendatasoft.com/api/records/1.0/search/?dataset=eco2mix-metropoles-tr&q=&timezone=Europe%2FParis"
    r=requests.get(url2)
    #r=requests.get('https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1000&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&facet=coverflow&facet=creditcard&facet=overflowactivation&facet=kioskstate&facet=station_state')
    velib=r.json()

    #print(velib)
    dbname = get_database()

    dbname.test_collection2.delete_many({})
    dbname.test_collection2.insert_many(velib['records'])
    #data=dbname.test_collection2.find()
    #data1=[d["fields"]["prod_journaliere_mwh_pcs"] for d in data]
   
    #print(data1)
    #return HttpResponse("Hello, world. You're at the index.")
    return HttpResponse("Hello, world. You're at the index.")



