# connect to mongodb
import json
from django.http import HttpResponse
from pymongo import MongoClient
import requests
from django.shortcuts import render
import datetime 
from project_linux.services import get_database



def home(request):
    return render(request, 'dashboard/home.html')
    
def gaz_function(request):
    dbname = get_database()

    data=dbname.test_collection.find()
    data1=[]
    data2=[]
    i=0
    for d in data:
        if i==1900:
            data1.append(d["fields"]["prod_journaliere_mwh_pcs"])
            data2.append(d["fields"]["journee_gaziere"])
        else:
            i=i+1
    context={
        'data':data1,
        'dataa':data2,
    }
    return render(request, 'dashboard/page_gaz.html',context)


def electricity_function(request):

    dbname = get_database()

    data=dbname.test_collection2.find()
    data1 = []
    data2 = []
    cpt=0
    
    for d in data:
        date_time_str = d["fields"]["date_heure"]
        date = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S%z').date().strftime('%Y-%m-%d')

        consommation = d["fields"].get("consommation", 0)

        try:
            if d["fields"]["consommation"] != None:
                cpt=cpt+1
        except:
            continue

        if date in data2:
            data1[data2.index(date)] += consommation
        else:
            data1.append(consommation)
            data2.append(date)
    context={
        'data':data1,
        'dataa':data2,
    }
    return render(request, 'dashboard/page_electricite.html',context)


def gazCombine_function(request):

    dbname = get_database()
    data=dbname.test_collection3.find()

    data1 = []
    data2 = []
    cpt=0
    
    for d in data:
        date_time_str = d["fields"]["jourcalendaire"]
        date = datetime.datetime.strptime(date_time_str,'%Y-%m-%d').date().strftime('%Y-%m-%d')

        consommation = d["fields"]["consommation_horaire"] if "consommation_horaire" in d["fields"] else 0


        if d["fields"]["consommation_horaire"] != None:
            cpt=cpt+1

        if date in data2:
            data1[data2.index(date)] += consommation
        else:
            data1.append(consommation)
            data2.append(date)
    context={
        'data':data1,
        'dataa':data2,
    }
    return render(request, 'dashboard/page_gazCombine.html',context)




