#json permet de créer et de lire des données au format json
import json
#import de la classe utilisée comme objet de retour d'une vue Django
from django.http import HttpResponse
#import de la classe MongoClient qui permet d'établir des connexions au serveur MongoDB
from pymongo import MongoClient
#import du module requests qui nous permet d'envoyer des requêtes HTTP à l'aide de Python.
import requests
#import de la fonction render qui permet de renvoyer un objet HttpResponse du modèle donné, rendu avec le contexte donné.
from django.shortcuts import render
#import du module datetime qui permet la manipulation de dates et d'heures.
import datetime 
#import de la fonction get_database du fichier services
from project_linux.services import get_database




"""
definition de la fonction home qui permet d'afficher la page d'accueil
parametre: request
return : la page d'acceuil du site
"""
def home(request):
    return render(request, 'dashboard/home.html')


"""
definition de la fonction gaz_function qui permet d'importer les données depuis mongoDB 
dans la collection 'test_collection' representant les données de la production du gaz
parametre: request
return : la page de la production du gaz 
"""
def gaz_function(request):
    #appel de la fonction get_database()
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


"""

definition de la fonction electricity_function qui permet d'importer les données depuis mongoDB
dans la collection 'test_collection2' representant les données de la consommation d'electricite
parametre: request
return : la page de la consommation d'electricite

"""
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
    print(context)
    return render(request, 'dashboard/page_electricite.html',context)


"""
definition de la fonction gazCombine_function qui permet d'importer les données depuis mongoDB
dans la collection 'test_collection3' representant les données de la consommation de gaz du biométhane
parametre: request
return : la page de la consommation de gaz du biométhane

"""
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




