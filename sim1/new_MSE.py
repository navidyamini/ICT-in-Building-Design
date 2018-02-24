# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:53:07 2018

@author: Navid
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def MSE(target,domain,title):
    #design matrix, phi, N X M
    N = len(domain)
    phi = np.array([np.ones(N),domain]).T
    #find the solution
    #in this case case phi.T X phi is invertible so do the folloing:
    temp1 = np.linalg.inv(np.dot(phi.T,phi)) #inverse of phi.T X phi
    temp2 = np.dot(temp1, phi.T)
    w1 = np.dot(temp2,target) #solution
    print ('w1=',w1)
    #assuming that phi.T X phi was not invertible we could find the pseudo inverse using the pinv function
    #we expect to obtain the same solution
    phi_pi = np.linalg.pinv(phi)
    w2 = np.dot(phi_pi,target)
    print ('w2=',w2)
  
    predicted_t = [w2[0]+w2[1]*x for x in domain]
    
    error = []
    for i in range(len(predicted_t)):
        e = (math.fabs(predicted_t[i] - target[i]))**2
        error.append(e)
    
    plt.plot(domain,target)
    plt.plot(domain,predicted_t)
    plt.title(title)
    plt.xlabel("Density")
    plt.ylabel("Q [kwh/m^2]")
    #plt.legend(loc=3)
    plt.show()
    return w2,predicted_t,error

def test(target,domain,w,title):
    predicted_t = [w[0]+w[1]*x for x in domain]
    error = []
    for i in range(len(predicted_t)):
        e = (math.fabs(predicted_t[i] - target[i]))**2
        error.append(e)
    
    plt.plot(domain,target,marker='.')
    plt.plot(domain,predicted_t)
    plt.title(title)
    plt.xlabel("Density")
    plt.ylabel("Q [kwh/m^2]")
    #plt.legend(loc=3)
    plt.show()
    return predicted_t,error

def write_output(result,error,name,sim_no,density_range):
    outfile = open(name+".txt", "w")
    outfile.write("density" + "," +"result" + "," + "error")
    outfile.write("\n")
    density=[]
   
    for i in range(sim_no):
        density.append(1000+(i*density_range))
        outfile.write(str(density[i])+","+str(result[i])+","+str(error[i]))
        outfile.write("\n")
    outfile.close()

if __name__ == "__main__":
   
    num_train=120
    numb_test=40
    density_train=50
    density_test = 174
    
    file_name = "F:/Polito/ICTinBuildingdesign/Building_project/ouput1.txt"
    data = pd.read_csv(file_name)
    
    domain = data["density"]
    target_cooling = data["cooling"]
    target_heating = data["heating"]           
           
    w_cooling,result_cooling,error1 = MSE(target_cooling ,domain,"cooling_sim1")
    w_heating,result_heting,error2 = MSE(target_heating ,domain,"heating_sim1")
    
    write_output(result_cooling,error1,"result_cooling_sim1",num_train,density_train)
    write_output(result_heting,error2,"result_heating_sim1",num_train,density_train)
    
    file_test = "F:/Polito/ICTinBuildingdesign/Building_project/ouput1_test.txt"
    testData = pd.read_csv(file_test)
    
    domain_test = testData["density"]
    target_cooling_test = testData["cooling"]
    target_heating_test = testData["heating"]
    
    result_cooling_test,error1_test = test(target_cooling_test ,domain_test,w_cooling,"cooling_test 1")
    result_heting_test,error2_test = test(target_heating_test ,domain_test,w_heating,"heating_test 1")
    
    write_output(result_cooling_test,error1_test,"result_cooling_test 1",numb_test,density_test)
    write_output(result_heting_test,error2_test,"result_heating_test 1",numb_test,density_test)
   

