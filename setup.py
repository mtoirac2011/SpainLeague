from multiprocessing.spawn import prepare
from src.ligatools import *
from src.menus import *
from src.laliga import *
from src.realmadrid import *
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
            case 'X':    
                menuGoodBye()

main()