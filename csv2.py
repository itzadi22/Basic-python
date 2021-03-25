# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:40:55 2021

@author: ASUS
"""

import csv
from datetime import datetime
bikelist=[]
with open("capital-onebike.csv","r")as file:
    reader=csv.reader(file)
    header=next(reader)
    for row in reader:
        bikelist.append(row[1])
        print(row[1])
        
race={"AM":0,"PM":0}  

for event in bikelist:
    bikerace=datetime.strptime(event, "%j-%m-%Y %H:%M").time()
    if bikerace.hour < 12:
        race["AM"]+=1
    else:
        race["PM"]+=1
        
print(race)        