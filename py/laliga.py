from traceback import print_list
from py.ligatools import *
from py.menus import *
from os import system
import csv

ligalist = []

class ListaLiga():
    
    def __init__(self):
        pass
        
def positionstable():
    #Work with the liga espanola table file
    try:
        with open('data/2018laliga.csv', newline='') as f:
            datos = csv.reader(f, delimiter=',')
            ligalist = list(datos)
            positionsTablePrint(ligalist)
    except:
        print("The file does not exists...\n")        

    pressAnyKey()
