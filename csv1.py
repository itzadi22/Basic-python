# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:17:19 2021

@author: ASUS
"""

import csv
from datetime import datetime
onebike=[]
with open("capital-onebike.csv","r")as file:
    reader=csv.reader(file)
    header=next(reader)
    for row in reader:
        onebike.append(row[0])
        print(row[0])
        
#create dictionary to hold results
eventtime={"AM":0,"PM":0}

#loop overall trips
for events in onebike:
    race = datetime.strptime(events,"%j-%m-%Y %H:%M").time()
    if race.hour < 12:
        eventtime["AM"] +=1
    else:
        eventtime["PM"] +=1
        
        
print(eventtime)





    