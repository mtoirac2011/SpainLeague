from traceback import print_list
from py.ligatools import *
from py.menus import *
import csv

# Check if log file exists    
checklogfile()
         
#Work with the liga espanola table file
with open('data/2018laliga.csv', newline='') as f:
    datos = csv.reader(f, delimiter=',')
    
    listaliga = list(datos)

welcomeMenu()
menuLiga()
menuClub()
