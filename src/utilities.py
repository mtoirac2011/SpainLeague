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
        print("Connection created ...")
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

    print(mydict)     
    pressAnyKey()