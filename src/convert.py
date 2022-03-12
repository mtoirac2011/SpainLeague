from traceback import print_list
from src.ligatools import *
from src.menus import *
from os import system
import csv
import operator
import re

class Convert():
    
    def __init__(self, value):
        self.value = value
    
def if_integer(string):

    reg_exp = "[-+]?\d+$"
    return re.match(reg_exp, string) is not None

def farToCelcious(value):
    return ((value - 32.0) * 5 / 9).ToString()                

def milesToKm(value):
    return (value * 1.60934).ToString()                

def feetToMeter(value):
    return (value * 0.3048).ToString() 

def meterToCm(value):
    return (value * 100).ToString() 

def doconvert(value):
    doConvertPrint(value)
    
    pressAnyKey()