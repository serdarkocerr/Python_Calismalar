# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 02:47:48 2022

@author: Serdar
Constant Velocity Kalman Filter Implementation
"""

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


print("test")

#Kalman predict equation
def predict(delta_time,prev_estimated_state,prev_estimated_uncertanity,std_acceler):
    
   F=getFMatrix(delta_time)            
   Q=getQMatrix(delta_time,std_acceler)   
   
   #print("F Matrix : ",F)
   #print("Q Matrix : ",Q)
   
   x_pred = np.dot(F,prev_estimated_state)
   p_pred_tmp = np.dot(F,prev_estimated_uncertanity)
   p_pred_tmp = np.dot(p_pred_tmp,np.transpose(F))
   p_pred = p_pred_tmp + Q
   
   return x_pred,p_pred
def update(x_pred,p_pred,z_measurement_current,r_measurement_uncertainty):
    #H mean what output  will occur after calculation. (x position , y position) if z 2 X 1 and x_pred 6 X 1, H should be 2X6
    H=[[1,0,0,0,0,0],
       [0,0,0,1,0,0]]
    I=np.identity(6)
    
    calculated_kalman_gain_1 = np.dot(p_pred,np.transpose(H))
    calculated_kalman_gain_2 = np.dot(np.dot(H,p_pred),np.transpose(H)) + r_measurement_uncertainty
    calculated_kalman_gain = np.dot(calculated_kalman_gain_1,np.linalg.inv(calculated_kalman_gain_2))
    x_est = x_pred + np.dot(calculated_kalman_gain,(z_measurement_current- np.dot(H,x_pred)))
    p_uncerainty_est_1 = np.dot((I - np.dot(calculated_kalman_gain,H)),p_pred)
    p_uncerainty_est_2 = np.dot(p_uncerainty_est_1,np.transpose((I -np.dot(calculated_kalman_gain,H) )))
    p_uncerainty_est = p_uncerainty_est_2 + np.dot(calculated_kalman_gain,np.dot(r_measurement_uncertainty,np.transpose(calculated_kalman_gain)))
    
    return x_est,p_uncerainty_est, calculated_kalman_gain
    
def getFMatrix(delta_time):
   F =np.zeros((6,6))
   
   for index,x in np.ndenumerate(F):
       #print(index[1],x)
       if(index[0]==0):
           if(index[1]==0):
               F[index[0]][index[1]]=1
           elif(index[1]==1):
               F[index[0]][index[1]]=delta_time
           elif(index[1]==2):
               F[index[0]][index[1]]=np.square(delta_time)*0.5
       #print(index[1],x)
       if(index[0]==1):
           if(index[1]==1):
               F[index[0]][index[1]]=1
           elif(index[1]==2):
               F[index[0]][index[1]]=delta_time
       if(index[0]==2):
           if(index[1]==2):
               F[index[0]][index[1]]=1
               
       if(index[0]==3):
           if(index[1]==3):
               F[index[0]][index[1]]=1
           elif(index[1]==4):
               F[index[0]][index[1]]=delta_time
           elif(index[1]==5):
               F[index[0]][index[1]]=np.square(delta_time)*0.5   
       if(index[0]==4):
           if(index[1]==4):
               F[index[0]][index[1]]=1
           elif(index[1]==5):
               F[index[0]][index[1]]=delta_time               
       if(index[0]==5):
           if(index[1]==5):
               F[index[0]][index[1]]=1     
   return F

def getQMatrix(delta_time,std_acceler):
   Q=np.zeros((6,6))
   Q[0][0]=(1/4)*(np.power(delta_time,4))*np.power(std_acceler,2)
   Q[0][1]=(1/2)*(np.power(delta_time,3))*np.power(std_acceler,2)
   Q[0][2]=(1/2)*(np.power(delta_time,2))*np.power(std_acceler,2)
  
   Q[1][0]=(1/2)*(np.power(delta_time,3))*np.power(std_acceler,2)
   Q[1][1]=(1)*(np.power(delta_time,2))*np.power(std_acceler,2)
   Q[1][2]=delta_time

   Q[2][0]=(1/2)*(np.power(delta_time,2))*np.power(std_acceler,2)
   Q[2][1]=delta_time*np.power(std_acceler,2)
   Q[2][2]=1*np.power(std_acceler,2)

   Q[3][3]=(1/4)*(np.power(delta_time,4))*np.power(std_acceler,2)
   Q[3][4]=(1/2)*(np.power(delta_time,3))*np.power(std_acceler,2)
   Q[3][5]=(1/2)*(np.power(delta_time,2))*np.power(std_acceler,2)
  
   Q[4][3]=(1/2)*(np.power(delta_time,3))*np.power(std_acceler,2)
   Q[4][4]=(1)*(np.power(delta_time,2))*np.power(std_acceler,2)
   Q[4][5]=delta_time*np.power(std_acceler,2)

   Q[5][3]=(1/2)*(np.power(delta_time,2))*np.power(std_acceler,2)
   Q[5][4]=delta_time*np.power(std_acceler,2)
   Q[5][5]=1*np.power(std_acceler,2)

   return Q    

def getRealPositions():
    y = []
    x = []
    for i in range(36):
        if(i < 20):
            y.append(300)  
            x.append(i *20 + (-400))  
        else:
                tmp1=math.pow(300, 2)
                tmp2= math.pow(((i-19) * 18.75),2) # 35-19 = 16, 300/16 = 18.75
                tmp = [tmp1 - tmp2]
                y_test_tmp = math.sqrt(tmp[0])
                y.append( y_test_tmp)
                x.append(i *20 + (-400)) 

    return x,y

    
def main():
    delta_time = 1#1 sec
    std_acceleration = 0.2# meter/sec^2
    std_measurement_error_xm=3#meter
    std_measurement_error_ym=3#meter
    initial_x_vector = np.array([0,0,0,0,0,0]) # x,Vx,ax, y,Vy,ay
   # initial_x_vector = initial_x_vector.transpose()
    #print(initial_x_vector.shape)
    initial_estimate_uncertainty = np.array([[500,0,0,0,0,0],
                                            [0,500,0,0,0,0],
                                            [0,0,500,0,0,0],
                                            [0,0,0,500,0,0],
                                            [0,0,0,0,500,0],
                                            [0,0,0,0,0,500]])
    # x and y
    z_measurement_values_meters = [[-393.66,-375.93,-351.04,-328.96,-299.35,-273.36,-245.89,-222.58,-198.03,-174.17,-146.32,-123.72,-103.47,-78.23,-52.63,-23.34,25.96,49.72,76.94,95.38,119.83,144.01,161.84,180.56,201.42,222.62,239.4,252.51,266.26,271.75,277.4,294.12,301.23,291.8,299.89],
                            [300.4,301.78,295.1,305.19,301.06,302.05,300,303.57,296.33,297.65,297.41,299.61,299.6,302.39,295.04,300.09,294.72,298.61,294.64,284.88,272.82,264.93,251.46,241.27,222.98,203.73,184.1,166.12,138.71,119.71,100.41,79.76,50.62,32.99,2.14]]
    
    # output matrix size 2x2 (measurement size) also same row size with H matrix (R should have row x row)
    r_measurement_uncertainty=[[ np.power(std_measurement_error_xm,2),0],[0,np.power(std_measurement_error_ym,2)]]
    
    x_est_list=[]
    y_est_list=[]
    #print(initial_estimate_uncertainty.shape)
    x_pred, p_pred = predict(delta_time,initial_x_vector,initial_estimate_uncertainty,std_acceleration)
    #x_estimated, p_uncerainty_estimated, kalman_estimated = update(x_pred,p_pred,[-393.66 , 300.4],r_measurement_uncertainty)
    column_len = len(z_measurement_values_meters[0])
    for i in range(column_len):
        z_measurement=[z_measurement_values_meters[0][i],z_measurement_values_meters[1][i]]
        x_estimated, p_uncerainty_estimated, kalman_estimated = update(x_pred,p_pred,z_measurement,r_measurement_uncertainty)
        x_pred, p_pred = predict(delta_time,x_estimated,p_uncerainty_estimated,std_acceleration)
        x_est_list.append(x_estimated[0])
        y_est_list.append(x_estimated[3])
    
    
    # print("x_pred Matrix : ")
    # print(x_pred)
    # print("p_pred Matrix : ")
    # print(p_pred)
    # print("x_estimated Matrix : ")
    # print(x_estimated)
    # print("p_uncerainty_estimated Matrix : ")  
    # print(p_uncerainty_estimated)
    # print("kalman_estimated Matrix : ")
    # print(kalman_estimated)
    
    
    x_real_positions,y_real_positions = getRealPositions()
    plt.plot(x_real_positions,y_real_positions, color='red',label='real_position')
    plt.plot(x_est_list,y_est_list, color='blue',label='estimated_position',marker='*')
    plt.plot(z_measurement_values_meters[0],z_measurement_values_meters[1], color='green',label='measured_position',marker='+')
    plt.legend()
    plt.plot()
    plt.show()
    
main()    