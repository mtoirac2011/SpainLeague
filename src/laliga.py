from traceback import print_list
from src.ligatools import *
from src.menus import *
from os import system
import csv
import operator

#ligalist = []

class ListaLiga():
    
    def __init__(self):
        pass
        
def positionsTable():
    #Work with the liga espanola table file
    try:
        with open('data/2018laliga.csv', newline='') as f:
            datos = csv.reader(f, delimiter=',')
            #Avoid Header
            headings = next(datos)              
            positionsTablePrint(list(datos))
    except:
        print("The file does not exists...\n")        

    pressAnyKey()

def moreShots():
    #Work with the liga espanola table file
    try:
        with open('data/2018laliga.csv', newline='') as f:
            datos = csv.reader(f, delimiter=',')
            #Avoid Header
            headings = next(datos)  
            sortList = list(datos)               
            moreShotsPrint(sorted(sortList , key=operator.itemgetter(11), reverse=True))
    except:
        print("The file does not exists...\n")        

    pressAnyKey()
    
