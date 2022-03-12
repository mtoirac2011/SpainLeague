from traceback import print_list
from src.ligatools import *
from src.menus import *
from os import system
import csv
import operator

class Convert():
    def __init__(self, value):
        self.value = value

def doconvert(value):
    doConvertPrint(value)
    pressAnyKey()