import os
import time
from src.menus import *
import re

def checklogfile():
    # Check if log file exists
    fileName = r"docs/filelog.txt"
    existslogfile = os.path.isfile(fileName)

    if existslogfile:
        print('The log file already exists, and it is ready to be used... ')
    else:
        try:
            with open('docs/filelog.txt', 'w') as f:
                f.write('Creating the log file!, ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+ '\r\n')
        except FileNotFoundError:
            print("The 'docs' directory does not exist...")  

def printlogfile(texto):
    with open('docs/filelog.txt', 'a') as f:
        f.write(texto +', ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\r')
            
def pressAnyKey():
    print("")
    input("     Press any key to continue...")

def positionsTablePrint(ligalist):
    positionsTableHeader()
    try: 
        for i in range(len(ligalist)):
            print(ligalist[i][1].center(9), ligalist[i][2].ljust(15), ligalist[i][3].center(7),\
                ligalist[i][4].center(4), ligalist[i][5].center(5), ligalist[i][6].center(5),\
                ligalist[i][9].center(3))
        printlogfile("Table positions was printed")
    except:
        print("Error printing file...")
        printlogfile("Error printing table positions")

def moreShotsPrint(ligalist):
    moreShotsHeader()
    try: 
        for i in range(len(ligalist)):
            print(" ", ligalist[i][2].ljust(15), ligalist[i][11].center(5))
        printlogfile("Teams with more shots was printed")
    except:
        print("Error printing file...")   
        printlogfile("Error printing Teams with more shots") 
         
def listPlayersPrint(playerlist):
    listPlayersHeader()
    try: 
        for i in range(len(playerlist)):
            print(" " + playerlist[i][1].ljust(17), playerlist[i][2].ljust(6), playerlist[i][4].center(3))
        printlogfile("List of players was printed")
    except:
        print("Error listing players...")
        printlogfile("Error listing players")
        
def sortByAgePrint(playerlist):
    sortByAgeHeader()
    try: 
        for i in range(len(playerlist)):
            print(" " + playerlist[i][1].ljust(17), playerlist[i][4].center(3))
        printlogfile("Oldest players was printed")
    except:
        print("Error printing oldest players...")
        printlogfile("Error listing oldest players")
        
def groupByNation(nationslist):
    res = [] 
    temp = dict() 
    try:
        for ele in nationslist: 
            if ele in temp: 
                temp[ele] = temp[ele] + 1 
            else :  
                temp[ele] = 1
        for key in temp: 
            res.append((key, temp[key])) 
        printlogfile("Grouping by nations done")
    except:
        print("Error grouping by nations....")
        printlogfile("Error grouping by nations....")
        
    return res

def groupByNationPrint(mytupla):
    groupNationHeader()
    try: 
        for nation in mytupla:
            print(" " + nation[0].ljust(9), str(nation[1]).center(6))
        printlogfile("Players by nation were printed")
    except:
        print("Error printing players by by nations...")
        printlogfile("Error printing players by nations ...")

def if_integer(string):
    
    reg_exp = "[-+]?\d+$"
    return re.match(reg_exp, string) is not None

def farToCelcious(value):
    return str(round((value - 32.0) * 5 / 9, 2))         

def milesToKm(value):
    return str(round(value * 1.60934, 2))              

def feetToMeter(value):
    return str(round(value * 0.3048, 2))

def meterToCm(value):
    return str(round(value * 100, 2))

def doConvertPrint(value):
    doConvertPrintHeader()
    try: 
        print("        You typed:     ", str(value))
        print("──────────────────────────────")
        print("Fahrenheit to celsius: ", farToCelcious(value))
        print("Miles to kilometers:   ", milesToKm(value))
        print("Feet to meters:        ", feetToMeter(value))
        print("Meters to centimeters: ", meterToCm(value))
        print("──────────────────────────────")
        printlogfile("Convertions were printed")
    except:
        print("Error printing convertions...")
        printlogfile("Error printing convertions")
