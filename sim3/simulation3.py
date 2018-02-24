from eppy.modeleditor import IDF
import numpy as np
import subprocess as sp
import pandas as pd
from matplotlib import pyplot as plt

def run_simulation():

    for i in range(120):
        output = 'F:\\Polito\\ICTinBuildingdesign\\Final\\sim3\\output\\\\' + str(i)
        weather = 'C:\\EnergyPlusV8-8-0\\WeatherData\\\\ITA_TORINO-CASELLE_IGDG.epw'
        idf = 'F:\\Polito\\ICTinBuildingdesign\\Final\\sim3\\'+ str(i)+'.idf'
        result = sp.run(['C:\\EnergyPlusV8-8-0\\energyplus', '-d', output, '-w', weather, idf], stdout=sp.PIPE)
        # print(result.stdout.decode('utf-8'))
        print(str(i)+" simulated")

run_simulation()