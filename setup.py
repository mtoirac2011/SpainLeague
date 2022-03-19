from multiprocessing.spawn import prepare
from src.ligatools import *
from src.menus import *
from src.laliga import *
from src.realmadrid import *
from src.convert import *
from src.utilities import *
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
            
def realMadrid():
    rm_menu = ''
    while (rm_menu != 'X'):
        menuRM()
        rm_menu = input("Choose the option: ").upper()
        match rm_menu:
            case 'P':
                listPlayers()
            case 'O':
                sortByAge()
            case 'N':
                sortByNation()               

def convert():
    convert_menu = ''
    while (convert_menu != 'X'):
        convertMenu()
        convert_menu = input("           Type a number: ").upper()        
        if (if_integer(convert_menu)):
            if int(convert_menu) > 0:
                doconvert(int(convert_menu))
                
def utilities():
    util_menu = ''
    while (util_menu != 'X'):
        utilitiesMenu()
        util_menu = input("Choose the option: ").upper()
        match util_menu:
            case 'S':
                selectPlayer()
            case 'N':
                sortByNation() 
                        
def main():
    main_menu = ''
    welcomeMenu()
    pressAnyKey()
    while (main_menu != 'X'):
        mainMenu()
        main_menu = input("Choose the option: ").upper()
        match main_menu:
            case 'L':
                laliga()
            case 'R':
                realMadrid()
            case 'C':
                convert()
            case 'U':
                utilities()
            case 'X':    
                menuGoodBye()


main()