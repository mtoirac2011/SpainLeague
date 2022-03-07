import os
import time
from py.menus import *

def checklogfile():
    # Check if log file exists
    fileName = r"docs/filelog.txt"
    existelogfile = os.path.isfile(fileName)

    if existelogfile:
        input('The log file already exists, and it is ready to be used... ')
    else:
        try:
            with open('docs/filelog.txt', 'w') as f:
                f.write('Creating the log file!, ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+ '\r\n')
        except FileNotFoundError:
            input("The 'docs' directory does not exist...")  

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

def moreShotsPrint(ligalist):
    moreShotsHeader()
    try: 
        for i in range(len(ligalist)):
            print(" ", ligalist[i][2].ljust(15), ligalist[i][11].center(5))
        printlogfile("Teams with more shots was printed")
    except:
        print("Error printing file...")    