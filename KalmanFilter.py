#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
#read csv file that have a column where data format is  json using quotechar="'" . (json_value column)
df = pd.read_csv('C:\\Users\\Serdar\\Desktop\\test.csv',header=0, quotechar="'",doublequote=False)
df.head()
print(df.columns)
print(df.size)
print(len(df))
df['json_value'] = df['json_value'].str.replace('""','"')#replacing  added doublequote json keys after  read_csv
df['time'] = df['time'].str.replace('"','')#replacing  added doublequote json keys after  read_csv 
df['key'] = df['key'].str.replace('"','')#replacing  added doublequote json keys after  read_csv 

df.head()


# In[2]:


#Normalize JSON column for place each elements set as column
df_json = pd.json_normalize(df.value.apply(json.loads))
df_json.head()


# In[3]:


#drop json_value column and  add JSON elements as columns
df = df.drop('json_value', axis=1)
print(df.columns)
df = pd.concat([df, df_json], axis=1)
df.head()


# In[4]:


#Find out each spec column length (spec column is array)
spec_lengths = {} #empty dictionary
for i in range(df.spec.size):
    length = len(df.spec[i])
    dict_value = spec_lengths.get(length, None)# default = None
    if(dict_value is None):
        new_record = {length:0} 
        spec_lengths.update(new_record) #adding new record
        
    spec_lengths[length] +=1
    
print(spec_lengths)


# In[5]:


#KALMAN IMPLEMENTATION
import numpy as np

#initial Kalman Values
measurement_kalman_gain = 0.0
error_kalman_gain  = 0.0

estimated_measurement = 0.0
estimated_error  = 0.0
pre_estimated_measurement = 0.0
pre_estimated_error  = 0.0

error_covariance = np.array([[1.0, 1.0],[1.0,1.0]])
pre_error_covariance = np.array([[1.0, 1.0],[1.0,1.0]])
#measured_value = 0
#measured_value_persecond = measured_value

time_interval = 1.0
noise_variance = 0.9
error_variance = 0.9

measurement_variance = 0.9
now = 0
last = 0

def calculatePreEstimateValue(measured_value_persecond):
    global estimated_measurement,estimated_error,pre_estimated_error, estimated_error,pre_estimated_measurement,time_interval
    print("before calculatePreEstimateValue - measured_value_persecond : " ,measured_value_persecond)
    print("before calculatePreEstimateValue - estimated_measurement : " ,estimated_measurement)
    print("before calculatePreEstimateValue - pre_estimated_measurement : " ,pre_estimated_measurement)
    
    estimated_measurement = pre_estimated_measurement + time_interval*(measured_value_persecond - pre_estimated_error)
    estimated_error = pre_estimated_error
    
    print("after calculatePreEstimateValue - estimated_measurement : " ,estimated_measurement)
    print("after calculatePreEstimateValue - estimated_error : " ,estimated_error)
    print("after calculatePreEstimateValue - pre_estimated_measurement : " ,pre_estimated_measurement)

    

    
def calculatePreErrorCovariance( ):
    global error_covariance, time_interval, time_interval, pre_error_covariance
    print("before calculatePreErrorCovariance - error_covariance : " ,error_covariance)
    error_covariance[0][0] += time_interval*(time_interval*pre_error_covariance[1][1] - pre_error_covariance[0][1] - pre_error_covariance[1][0] + measurement_variance )
    error_covariance[0][1] -= time_interval*pre_error_covariance[1][1]
    error_covariance[1][0] -= time_interval*pre_error_covariance[1][1]
    error_covariance[1][1] += time_interval*time_interval
    print("after calculatePreErrorCovariance - error_covariance : " ,error_covariance)

    

def calculateKalmanGain():
    global measurement_kalman_gain, error_covariance, noise_variance, error_kalman_gain
    print("before calculateKalmanGain - measurement_kalman_gain : " ,measurement_kalman_gain)
    print("before calculateKalmanGain - error_kalman_gain : " ,error_kalman_gain)
    
    measurement_kalman_gain = error_covariance[0][0] / (error_covariance[0][0] + noise_variance )
    #measurement_kalman_gain = 0.5 # if kalman gain = 0.5, it means average.
    error_kalman_gain = error_covariance[1][0] / (error_covariance[0][0] + noise_variance)
    
    print("after calculateKalmanGain - measurement_kalman_gain : " ,measurement_kalman_gain)
    print("after calculateKalmanGain - error_kalman_gain : " ,error_kalman_gain)

def calculateErrorCovariance():
    global error_covariance, measurement_kalman_gain, error_kalman_gain, pre_error_covariance
    print("before calculateErrorCovariance - error_covariance : " ,error_covariance)
    print("before calculateErrorCovariance - pre_error_covariance : " ,pre_error_covariance)
    
    error_covariance[0][0] -=(measurement_kalman_gain*error_covariance[0][0])
    error_covariance[0][1] -= (measurement_kalman_gain*error_covariance[0][1])
    error_covariance[1][0] -= (error_kalman_gain*error_covariance[0][0])
    error_covariance[1][1] -= (error_kalman_gain*error_covariance[0][1])
    for i in range(2):
        for k in range(2):
            pre_error_covariance[i][k] = error_covariance[i][k]
    print("after calculateErrorCovariance - error_covariance : " ,error_covariance)            
    print("after calculateErrorCovariance - pre_error_covariance : " ,pre_error_covariance)

def calculateEstimatedValue(measured_value):
    global estimated_measurement,estimated_error,pre_estimated_measurement, pre_estimated_error,measurement_kalman_gain,error_kalman_gain
    print("before calculateEstimatedValue - estimated_measurement : " ,estimated_measurement)
    print("before calculateEstimatedValue - estimated_error : " ,estimated_error)
    print("before calculateEstimatedValue - pre_estimated_measurement : " ,pre_estimated_measurement)
    print("before calculateEstimatedValue - pre_estimated_error : " ,pre_estimated_error)

    estimated_measurement += measurement_kalman_gain*(measured_value - estimated_measurement)
    estimated_error += error_kalman_gain * (measured_value  - estimated_measurement)
    pre_estimated_measurement = estimated_measurement
    pre_estimated_error = estimated_error
    
    print("aftercalculateEstimatedValue - estimated_measurement : " ,estimated_measurement)
    print("after calculateEstimatedValue - estimated_error : " ,estimated_error)
    print("after calculateEstimatedValue - pre_estimated_measurement : " ,pre_estimated_measurement)
    print("after calculateEstimatedValue - pre_estimated_error : " ,pre_estimated_error)
    
def timeUpdate(measured_value):
    print(35*'*'+"Time Update - BEGIN " + 35*'*')
    calculatePreEstimateValue(measured_value)
    calculatePreErrorCovariance()
    print(35*'*'+"Time Update - END " + 35*'*')

def measurmentUpdate(measured_value):
    print(35*'*'+"Measurement Update - BEGIN " + 35*'*')

    calculateKalmanGain()
    calculateErrorCovariance()
    calculateEstimatedValue(measured_value)
    print(35*'*'+"Measurement Update - END " + 35*'*')
    
    return estimated_measurement
            
def KalmanFilter(measured_value):
    timeUpdate(measured_value )
    return measurmentUpdate(measured_value) 


# In[6]:


test_spec_array = np.array([-84,-85,-90,-88,-88,-89,-87,-85,-84,-87,-86,-85,-83,-84,-85,-84,-85,-88
,-91,-85,-84,-82,-84,-87,-86,-87,-88,-88,-89,-89,-85,-83,-84,-87,-84,-88
,-88,-90,-86,-86,-87,-10,-15,-14,-13,-15,--12,-11,-10,-9,-10,-12,-15,-20
,-22,-27,-35,-50,-86,-89,-87,-87,-86,-88,-88,-87,-87,-87,-86,-90,-90,-87
,-85,-83,-83,-83,-84,-84,-85,-85,-82,-81,-84,-89,-88,-88,-83,-82,-85,-85
,-85,-87,-88,-85,-83,-84,-86,-86,-85,-85])
KF_spec_test = []
for i in range(len(test_spec_array)):
    calculated = KalmanFilter(test_spec_array[i])
    KF_spec_test.append(calculated)
print(KF_spec_test) 


# In[8]:


#SHOW 
import matplotlib.pyplot as plt

plt.figure(0)
plt.figure(figsize=(10,5))

plt.plot(test_spec_array,"-b",label="spec") # plotting by columns
plt.scatter(range(len(test_spec_array)), test_spec_array,color='red')
plt.plot(KF_spec_test,label="KFSpec", color='green')
plt.legend(loc="upper left")
plt.xlabel('data', fontsize=18)
plt.ylabel('dBm', fontsize=16)
plt.title("Raw Spec. Data ")
plt.show()


# In[10]:


#Diff between measured and estimated
substract = np.subtract(test_spec_array, KF_spec_test)
substract


# In[ ]:




