#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#AVRO TO DATAFRAME
import csv
import string

input_file = open("C:\\Users\\Serdar\\Desktop\\test.csv", 'r')
output_file = open('C:\\Users\\Serdar\\Desktop\\testFixedBackslash.csv', 'w')
data = csv.reader(input_file)
writer = csv.writer(output_file)
specials = '\\'

for line in data:
    line = [value.replace(specials, '') for value in line]
    writer.writerow(line)

input_file.close()
output_file.close() 

#avro to dataframe
import pandas
import fastavro

def avro_df(filepath, encoding):
    # Open file stream
    with open(filepath, encoding) as fp:
        # Configure Avro reader
        reader = fastavro.reader(fp)
        # Load records in memory
        records = [r for r in reader]
        # Populate pandas.DataFrame with records
        df = pandas.DataFrame.from_records(records)
        # Return created DataFrame
        return df
    


# In[ ]:


#JSON Parsers or implement specific parser for dataframe column convertion to data what you desire
def CustomParser(data):
    import json
    j1 = json.loads(data)
    return j1
def parse_column(data):
    try:
        return json.loads(data)
    except Exception as e:
        print(e)
        return None


# In[ ]:



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


# In[ ]:


#Normalize JSON column for place each elements set as column
df_json = pd.json_normalize(df.value.apply(json.loads))
df_json.head()


# In[ ]:


#drop json_value column and  add JSON elements as columns
df = df.drop('json_value', axis=1)
print(df.columns)
df = pd.concat([df, df_json], axis=1)
df.head()


# In[ ]:


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


# In[ ]:


#Kalman Filtresi global tanımlar
X_k_KalmanTahminEski = 0 #Prior Estimate
Pk_HataKovaryansiEski = 1 #Error
R_HataMiktari = 3

def KalmanFiltresiHesapla(Zk_OlculenDeger, R_HataMiktari):
    #Güncelleme--Eski değerleri yeni değerler içine atıyor.
    global X_k_KalmanTahminEski, Pk_HataKovaryansiEski
    X_k_KalmanTahminYeni = X_k_KalmanTahminEski
    Pk_HataKovaryansiYeni =Pk_HataKovaryansiEski
    
    #Kk_KalmanKazanci = Pk_HataKovaryansiYeni /(Pk_HataKovaryansiYeni + R_HataMiktari)
    Kk_KalmanKazanci = 0.5 #kalman kazancı 05 ise ortalama alır.
    Xk_KalmanHesaplanan = X_k_KalmanTahminYeni+ Kk_KalmanKazanci * (Zk_OlculenDeger - X_k_KalmanTahminYeni)
    Pk_HataKovaryansiYeni = (1 - Kk_KalmanKazanci) *Pk_HataKovaryansiEski
    #Eski Değerleri Atama--bu değişkenler Global tanımlandı. bu procedure her geldiğinde bunları kaybetmemelidir.
    Pk_HataKovaryansiEski = Pk_HataKovaryansiYeni
    X_k_KalmanTahminEski = Xk_KalmanHesaplanan
    #bulunan sonuç bir sonraki adım için eski tahmin olacak.
    return Xk_KalmanHesaplanan


# In[ ]:


test=np.array([0.39, 0.50, 0.48, 0.29, 0.25, 0.32, 0.34, 0.48, 0.41, 0.45])
KF_sonuc= []

for i in range(len(test)):
    ret=KalmanFiltresiHesapla(test[i],R_HataMiktari)
    KF_sonuc.append(ret)

print(KF_sonuc)


# In[ ]:


import numpy as np

KF_spec= []
specList = []
for loop in range(2):
    specList = np.reshape(df.spec[loop],(-1,100))
    for spect in specList:
        for i in range(len(spect)):
            hesaplanan = KalmanFiltresiHesapla(spect[i],R_HataMiktari)
            KF_spec.append(hesaplanan)
            
    specList.append(df.spec[loop])
KF_spec = np.reshape(KF_spectrums,(-1,1))
print(KF_spectrums.shape)
specList = np.reshape(np.array(specList),(-1,1))
print(specList.shape)
print(KF_spec[100])
print(specList[100])


# In[ ]:


spectList = np.reshape(df.spec[loop],(-1,100))

for spect in spectList:
    print(spect)


# In[ ]:


import matplotlib.pyplot as plt

plt.figure(0)
plt.figure(figsize=(10,5))

plt.plot(spectrumList,"-b",label="spec") # plotting by columns
plt.scatter(range(len(spectrumList)), spectrumList,color='red')
plt.plot(KF_spectrums,label="KFSpect", color='green')
plt.legend(loc="upper left")
plt.xlabel('data', fontsize=18)
plt.ylabel('dBm', fontsize=16)
plt.title("Raw Spec Data ")
plt.show()


# In[ ]:


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


# In[ ]:


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


# In[ ]:


#Diff between measured and estimated
substract = np.subtract(test_spec_array, KF_spec_test)
substract

