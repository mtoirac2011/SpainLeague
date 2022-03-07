from traceback import print_list
from py.ligatools import *
from py.menus import *
from py.laliga import *
from os import system
import csv

#clean the screen
system("cls")

# Check if log file exists    
checklogfile()
        
def laliga():
    liga_menu = ''
    while (liga_menu != 'X'):
        menuLiga()
        liga_menu = input("Choose the option: ").upper()
        match liga_menu:
            case 'P':                
                positionsTable()
            case 'S':
                moreShots()
            case 'V':
                print ("Option L La Liga")

                
def realMadrid():
    rm_menu = ''
    while (rm_menu != 'X'):
        menuRM()
        rm_menu = input("Choose the option: ").upper()
        match rm_menu:
            case 'P':
                print ("Option L List of Players")
            case 'O':
                print ("Option R --> Oldest players")
            case 'N':
                print ("Option R --> Players by nation")

def main():
    main_menu = ''
    welcomeMenu()
    while (main_menu != 'X'):
        mainMenu()
        main_menu = input("Choose the option: ").upper()
        match main_menu:
            case 'L':
                print ("Option L La Liga")
                laliga()
            case 'R':
                print ("Option C --> Real Madrid")
                realMadrid()
            case 'X':    
                menuGoodBye()
                       
#Work with the liga espanola table file
#with open('data/2018laliga.csv', newline='') as f:
#datos = csv.reader(f, delimiter=',')
            
#listaliga = list(datos)

        
        #menuLiga()
        #menuRM()
    
#Execute main.py
main()