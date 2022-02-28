from traceback import print_list
from appligatools import *
import csv

# Check if log file exists    
checklogfile()
         
#Work with the liga espanola table file
with open('data/2018laliga.csv', newline='') as f:
    datos = csv.reader(f, delimiter=',')
    
    listaliga = list(datos)

print(' - -------  Socces teams final position ---------')
print('Position Team            Matches Wins Draw Loses Score \n')
for listaall in listaliga:
    print( listaall[1].center(8), listaall[2].ljust(15), " ", listaall[3].center(7), \
           listaall[4].center(4), listaall[5].center(5), listaall[6].center(5), listaall[7].center(6) )
print('\n')

