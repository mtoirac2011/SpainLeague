from traceback import print_list
from py.ligatools import *
from py.menus import *
import csv

def main():
    main_menu = ''
    welcomeMenu()
    while (main_menu != 'X'):
        menuLiga()
        main_menu = input("Choose the option: ").upper()
        match main_menu:
            case 'P':
                print ("Option P")
            case 'C':
                print ("Option C --> Corners")
            case 'S':
                print ("Option S --> Shots")
            case 'P':
                print ("Option P")
            
        # Check if log file exists    
        checklogfile()
                
        #Work with the liga espanola table file
        with open('data/2018laliga.csv', newline='') as f:
            datos = csv.reader(f, delimiter=',')
            
            listaliga = list(datos)

        
        #menuLiga()
        #menuClub()
    
#Execute main.py
main()