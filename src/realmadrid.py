from src.ligatools import *
from src.menus import *
from os import system
import csv
import operator
import pandas as pd
        
def listPlayers():
    try:
        with open('data/real_madrid_fc.csv', newline='') as f:
            datos = csv.reader(f, delimiter=',')
            #Avoid Header
            headings = next(datos)              
            listPlayersPrint(list(datos))
    except:
        print("The file does not exists...\n") 
        printlogfile("The file does not exists...")       

    pressAnyKey()
    
def sortByAge():
    try:
        with open('data/real_madrid_fc.csv', newline='') as f:
            datos = csv.reader(f, delimiter=',')
            #Avoid Header
            headings = next(datos)              
            sortByAgePrint(sortByAgeDesc(list(datos)))
    except:
        print("The file does not exists...\n")   
        printlogfile("The file does not exists")      

    pressAnyKey()
    
def sortByAgeDesc(playerlist):
    mylist=[]
    try:
        mylist = sorted(playerlist , key=operator.itemgetter(4), reverse=True)
    except:
        print("Error sorting player list...")  
        printlogfile("Error sorting player list")  
    
    returnList = []    
    for oldest in mylist:
        if int(oldest[4]) > 29:
            returnList.append(oldest) 
    
    return returnList

def sortByNation():
    try:
        with open('data/real_madrid_fc.csv', newline='') as f:
            datos = csv.reader(f, delimiter=',')
            #Avoid Header
            headings = next(datos)
            playerlist = list(datos) 
            
            #Sorting by nations
            mylist = sorted(playerlist , key=operator.itemgetter(2))
            nationslist=[]
            
            #Crear Nation column
            for player in mylist:
                nationslist.append(player[2])
            
            #Convert to a tuple with count by nation
            newtupla = groupByNation(nationslist)
            
            #Printing players by nation
            groupByNationPrint(newtupla)
    except:
        print("The file does not exists...\n")  
        printlogfile("The file does not exists")       

    pressAnyKey()