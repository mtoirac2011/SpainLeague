import pandas as pd
import numpy as np
import matplotlib as plt

valueToRead = input("Type a value: ")
print("The value is: "+ valueToRead)

#read csv file
players = pd.read_csv("data/real_madrid_fc.csv")

playerlist = []
#using print()
for player in players:
    playerlist.append(player)
    
for i in range(len(playerlist)):
    print(playerlist[i])
    
#view items
#players.head(2)
