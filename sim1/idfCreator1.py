# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:16:32 2018

@author: Navid
"""

from eppy.modeleditor import IDF
import numpy as np
import subprocess as sp
import pandas as pd
from matplotlib import pyplot as plt

#path to eenergy plud
iddfile = "C:/EnergyPlusV8-8-0/PreProcess/IDFVersionUpdater/V8-8-0-Energy+.idd"
#path to original .idf
fname1 = "F:/Polito/ICTinBuildingdesign/Final/sim1/sim1.idf"
IDF.setiddname(iddfile)
idf1 = IDF(fname1)

occupancy_density_room = 0.1110
occupancy_density_corridor = 0.080
std = 0.001

np.random.seed(0)

#idf1.printidf()
#print("**********************")

#Editing density of the wall,roof and the number of people

def create_idf():
    for i in range(120):
    #Density for wall and roof
        idf1.idfobjects['MATERIAL'][4].Density = 1000 +(i*50)
        #random noise(number of people inside)
        for j in range(6):
            density1 = np.random.normal(occupancy_density_room,std)
            density2 = np.random.normal(occupancy_density_corridor,std)

            if(j==1 or j==4):
                idf1.idfobjects['PEOPLE'][j].Number_of_People = idf1.idfobjects['ZONE'][j].Floor_Area * abs(density2)
                #print(abs(density2))
            else:
                idf1.idfobjects['PEOPLE'][j].Number_of_People = idf1.idfobjects['ZONE'][j].Floor_Area * abs(density1)
                #print(abs(density1))
        idf1.saveas(str(i)+'.idf')
        print(str(i) + "created")
        
create_idf()

print(idf1.idfobjects['MATERIAL'][4].Density)        