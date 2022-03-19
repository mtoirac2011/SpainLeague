from optparse import Values
from traceback import print_list
from src.ligatools import *
from src.menus import *
import pandas as pd 
import pyodbc
from os import system
import csv
import operator

class Utilities():
    def __init__(self, value):
        self.value = value
      
      
def loadTable():
    #Creating connection 
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=PC-MIN;'
                            'Database=laligadb;'
                            'Trusted_Connection=yes;')
        printlogfile("Creating connection to SQL Server...")
    except:
        print("Error creating connection ...")
        printlogfile("Error creating connection to SQL Server...")
        pressAnyKey()
    
    #Creating cursor   
    cursor = conn.cursor()
    
    #Executin query  
    cursor.execute('SELECT * FROM laligadb.dbo.t_realmadrid')
        
    #Creating a dict
    mydict = {}
    for row in cursor:
        mydict[row[0]] = row[1]

    return mydict    

def showPlayers(playerDict):
    until = len(playerDict)
    index=1
    while index <= len(playerDict):
        indexStr = str(index).ljust(2)
        indexMasUnoStr = str(index + 1).ljust(2)
        indexMasDosStr = str(index + 2).ljust(2)
        print(indexStr + " -> "+ playerDict[indexStr].ljust(17) +" │  "+ indexMasUnoStr + " -> "+ playerDict[indexMasUnoStr].ljust(17) +" │  "+ indexMasDosStr + " -> "+ playerDict[indexMasDosStr].ljust(17))
        
        if (index + 4) >= len(playerDict):
            index+=3
            indexStr = str(index).ljust(2)
            indexMasUnoStr = str(index + 1).ljust(2)
            indexMasDosStr = str(index + 2).ljust(2)

            if (index + 2) == len(playerDict):
                print(indexStr + " -> "+ playerDict[indexStr].ljust(17) +" │  "+ indexMasUnoStr + " -> "+ playerDict[indexMasUnoStr].ljust(17) +" │  "+ indexMasDosStr + " -> "+ playerDict[indexMasDosStr].ljust(17))
            elif (index + 1) == len(playerDict):
                print(indexStr + " -> "+ playerDict[indexStr].ljust(17) +" │  "+ indexMasUnoStr + " -> "+ playerDict[indexMasUnoStr].ljust(17))
            elif  index == len(playerDict):  
                print(indexStr + " -> "+ playerDict[indexStr].ljust(17))
                           
            break
        index+=3

def printBlankLines(num):
    i = 1
    while (num >= i):
        i+=1
        print()

def selectPlayer():
    system("cls")
    printBlankLines(10)
    print("                  Loading players from SQL Server ...")
    playerDict = {}
    playerDict = loadTable()

    #Showing players by screen...
    system("cls")
    print("Showing players by screen...")
    utility_menu = ''
    while (utility_menu != 'X'):
        #Show players to be selected
        system("cls")
        showPlayers(playerDict)    
    
        playerSelected = ' '
        playerName = ' '
        while True:
            print('')
            playerSelected = input("Select the player by choosing a valid number (x-Exit): ").upper()
            if (if_integer(playerSelected)):
                if (int(playerSelected) > 0 and int(playerSelected) < 36):                    
                    playerName = playerDict[playerSelected.ljust(2)]
                    
                    #Process
                    system("cls")
                    playerToShow = "You have selected: " + playerName
                    print(playerToShow.center(41))
                    print("┌─────────────────────────────────────────┐")
                    print("│                                         │")
                    print("│ Last letter:          "+playerName[len(playerName)-1]+"                 │")
                    print("│ First letter:         "+playerName[0]+"                 │")
                    print("│ Length of the Name:   "+ str(len(playerName)).center(2) +"                │")
                    print("│ Lower Case:           "+playerName.lower().ljust(17)+ " │")
                    print("│ Upper Case:           "+playerName.upper().ljust(17)+ " │")
                    print("│ Reversing the Name:   "+playerName[::-1].ljust(17)+" │")
                    print("│                                         │")
                    print("└─────────────────────────────────────────┘")
                    print('')
                    utility_menu = input("Do you want to select another player y/x? x-Exit ").upper()
                    break
            elif (playerSelected == 'X'):
                utility_menu = 'X'
                break

   