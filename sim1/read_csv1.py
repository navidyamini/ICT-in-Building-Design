from eppy.modeleditor import IDF
import numpy as np
import subprocess as sp
import pandas as pd
from matplotlib import pyplot as plt

def read_csv():
    cooling=[]
    heating=[]
    for i in range(120):
        csv_path = "F:/Polito/ICTinBuildingdesign/final/sim1/output/"+str(i)+"/eplustbl.csv"
        table = pd.read_csv(csv_path, header=None, skiprows=98, nrows=5)
        cooling.append(table.loc[2][5])
        heating.append(table.loc[2][6])
        print("read file"+str(i))
    return cooling,heating

cooling,heating = read_csv()
outfile = open("ouput1.txt", "w")
outfile.write("density" + "," +"cooling" + "," + "heating")
outfile.write("\n")
density=[]
for i in range(120):
    density.append(1000+(i*50))
    outfile.write(str(density[i])+","+str(cooling[i])+","+str(heating[i]))
    outfile.write("\n")

outfile.close()

plt.plot(density, cooling)
plt.title('cooling')
plt.grid(True)
plt.show()
