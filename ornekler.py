#!/usr/bin/env python
# coding: utf-8

# In[3]:


sayi = 1;
while(sayi<10):
    print(sayi)
    sayi = sayi+1


# In[4]:


for sayi in range(10):
    print(sayi)


# In[5]:


for sayi in range(1,10):
    print(sayi)


# In[6]:


for sayi in range(10,1,-1):
    print(sayi)


# In[7]:


basariNotu = 50;
if(basariNotu > 50):
    print("Basarili :)")
else:
    print("Basarisiz :(")


# In[8]:


isim =input("isminizi klavyeden giriniz ")
print(isim)


# In[9]:


sayi1 = int(input("sayi1 giriniz : "))
sayi2 = int(input("sayi2 giriniz : "))
print("sayi1 + sayi2  : " , sayi1+sayi2)


# In[10]:


import os
 
print ("Kullanıcı adı:  ", os.environ["USERNAME"])
print ("Bilgisayar adı: ", os.environ["COMPUTERNAME"])
print ("Ev dizini:      ", os.environ["HOMEPATH"])
print ("İşlemci:        ", os.environ["PROCESSOR_IDENTIFIER"])
print ("İşlemci sayısı: ", os.environ["NUMBER_OF_PROCESSORS"])
print ("İşletim sistemi:", os.environ["OS"])


# In[11]:


# harf sayılarının toplamı
from collections import Counter
print (Counter('bilisim sistemleri'))


# In[12]:


import sys
print (sys.version)


# In[15]:


### 2. slayt

def ekran_goruntu():
    print ("Sakarya Üniversitesi")
    print ("Bilgisayar ve Bilişim Bilimleri Fakültesi")
    print ("Sakarya")    
ekran_goruntu() #function call


# In[16]:


def toplamaIslemi(x, y):
    toplam = x + y
    ekran = ' {} ve {} sayılarının toplamı: {}.'.format(x, y, toplam)
    print(ekran)

def main():
    toplamaIslemi(10, 20) # parametre gönderilmesi
    toplamaIslemi(10000, 20000) # parametre gönderilmesi
    a = int(input("bir sayi giriniz: "))
    b = int(input("yeni bir sayi giriniz: "))
    toplamaIslemi(a, b) # parametre gönderilmesi

main() 


# In[21]:


def print_menu():
    print(35*"-" + "MENU" + 35*"-")
    print("sayi girmek için 1")
    print("sayilari toplamak için 2")
    print("sayilari çıkartmak için 3")
    print("sayilari çarpmak için 4")
    print("sayilari bölmek için 5")
    print("programdan çıkış için  6")
    print(70*"-")
 
donguDegiskeni = True
while(donguDegiskeni):
    print_menu()
    giris = int(input("islem giriniz:"))
    if(giris == 1):
        sayi1 = int(input("sayi1: "))
        sayi2 = int(input("sayi2: "))
    elif (giris == 2):
        print("toplamları : " , sayi1+sayi2)
    elif (giris == 3):
        print("farklari :" , sayi1-sayi2)
    elif (giris == 4):
        print("çarpımları: " , sayi1*sayi2)
    elif (giris == 5):
        print("bölümleri = ", sayi1/sayi2)
    elif (giris == 6):
        donguDegiskeni = False;
    else:
        print("yanlis sayi girdiniz. Tekrar giriniz.")


# In[22]:


liste = [i for i in range(10)]
print (liste)
print
liste = list(range(10))
print (liste)


# In[23]:


## HAFTA 3

sayilar = [0] * 10
print (sayilar)


# In[24]:


#range(start, stop, step)
for i in range(3, 16, 3):
    print(i)


# In[25]:


sicaklik_degerleri = [19, 10, 13, 12, 11, 9, 8]
hafta_ici = sicaklik_degerleri[0:5] 
print (sicaklik_degerleri)
print (hafta_ici)


# In[26]:


#SLICING - Dilimleme
sicaklik_degerleri = [19, 10, 13, 12, 11, 9, 8]
# bütün liste, sondan iki eleman hariç
hafta_ici = sicaklik_degerleri[-7:-2] 
print (sicaklik_degerleri)
print (hafta_ici)


# In[27]:


#SLICING - Dilimleme
hafta_ici=sicaklik_degerleri[-1]    # listedeki son eleman
print (hafta_ici)
hafta_ici=sicaklik_degerleri[-2:]   # listedeki son iki eleman
print (hafta_ici)
hafta_ici=sicaklik_degerleri[:-2]   # son iki eleman hariç bütün elemanlar
print (hafta_ici)


# In[48]:


#SLICING – Dilimleme
sicaklik_degerleri = [19, 10, 13, 12, 11, 9, 8]
hafta_ici=sicaklik_degerleri[::2]    # baştan sona kadar 0,2,4,6,8. elemanlar. 2 burada step demek.
print (hafta_ici)
hafta_ici=sicaklik_degerleri[::-1]    # Sondan başlayarak bütün elemanlar (-1 step ters git demektir.)
print (hafta_ici)
hafta_ici= sicaklik_degerleri[1::-1]   # Sondan başlayarak ilk iki eleman (-1 step ters git demektir.)
print (hafta_ici)
hafta_ici= sicaklik_degerleri[:-3:-1]  # Sondan başlayarak son iki elemanlar
print (hafta_ici)
hafta_ici= sicaklik_degerleri[-3::-1]  # Sondan başlayarak son iki eleman hariç
print (hafta_ici)
hafta_ici= sicaklik_degerleri[-3::1]  # Sondan başlayarak son iki eleman hariç
print (hafta_ici)


# In[47]:


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print (nums[-2:1:-1])
print (nums[-2:1:-3])
print (nums[1::-1])
print (nums[1:])
print (nums[-1::-1])


# In[51]:


def main():
    # Liste
    paket_isimleri = ['AX', 'GP', 'NAV', 'SL', 'CRM']

    # ekran çıktısı
    print('Listedeki veriler:')
    print(paket_isimleri)
    # ekran çıktısı
    print('Listedeki 2 veri:')
    print(paket_isimleri[2])
    
    # sıfırıncı elemanın silinmesi.
    paket_isimleri.remove('AX')
    print ("ilk eleman listeden silindi")
    print(paket_isimleri)

    # ekran çıktısı
    print('listedeki son elemanın silinmesi:')
    print(paket_isimleri)
    
    paket_isimleri.pop()
    print('Listeye veri silme:')
    print(paket_isimleri)

# Call the main function.
main()


# In[52]:


cars = ['bmw', 'audi', 'toyota', 'subaru', 'fiat']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse alphabetical list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)


# In[54]:


## HAFTA 4

tuple01=()  # boş bir tuple
a = (100)
print (a)


# In[55]:


tuple002 = (100, 200, 300, 350)

print (tuple002)
print (tuple002[-1])
print (tuple002[0:1]) 
print (tuple002[0:3])
print (tuple002[2])


# In[56]:


#tuple’a yeni eleman ilavesi
tuple003 = (100, 200, 300, 400)
print (tuple003)
yeniTuple = tuple003
yeniTuple += (500,)
tuple003 += (5000,)
print (yeniTuple)
print (tuple003)


# In[57]:


#İndex Oluşturma:
#Belli bir tuple elemanına erişebilmek için parantez içindeki konum numarası belirtilir. 
#Pozitif ve negatif indeksleme yapılabilir.
sicaklik_degeri = (10, 13, 14, 9, 8, 16, 11)
print (sicaklik_degeri[0])
print (sicaklik_degeri[2])

print (sicaklik_degeri[-1])
print (sicaklik_degeri[-6])


# In[59]:


#Tuple Sıralama(Ascending Order, Sorting)

sicaklik_degeri = (10, 13, 14, 9, 8, 16, 11)
sicaklik_degeri = sorted(sicaklik_degeri)
print (sicaklik_degeri)


# In[60]:


#Tuple Büyükten Küçüğe Sıralama(Descending Order, Sorting)

sicaklik_degeri = (10, 13, 14, 9, 8, 16, 11)
sicaklik_degeri = sorted(sicaklik_degeri, reverse = True)
print (sicaklik_degeri)


# In[64]:


liste= [10, 30, 50]
tuple=(60,65,70,"serdar")
print (liste)
print (tuple)
#veri elemanı değişikliği
liste[1]=100
#tuple[1]=300 #TypeError: 'tuple' object does not support item assignment
print (liste)
print (tuple)


# In[65]:


# tuple'ın 1. elemanını değiştirmek için

liste= [10, 30, 50]
tuple=(60,65,70)
print (liste)
print (tuple)
#veri elemanı değişikliği
liste[1]=100
#tuple[1] elemanın değerinin 300 olarak değiştirilmesi
n=1
tuple= tuple[ : n] + (300 ,) + tuple[n + 1 : ]
print (liste)
print (tuple)


# In[66]:


nested_tuple = (4, 5, 6), (7, 8, 9, 10)
print (nested_tuple)


# In[67]:


tuple=('sakarya', 'universitesi') * 4
print (tuple)


# In[68]:


tuple = (1, 2, 2, 2, 3, 4, 2, 3, 6, 8, 2)
print (tuple.count(2)) # 2 rakamının sayılması


# In[69]:


port = {22: "SSH", 23: "Telnet" , 53: "DNS", 80: "HTTP" }
print (port)


# In[70]:


ERP = {"AX": "MS AXAPTA", "NAV" :"MS Navision"}
print (ERP)
print (ERP['AX'])
print (ERP['NAV'])


# In[72]:


#copy() fonksiyonu
ERP = {"AX": "MS AXAPTA", "NAV" :"MS Navision", "SAP": "Systems Applications and Products"}
print
print (ERP)
print
print (ERP['AX'])
print (ERP['SAP'])
ERPDict=ERP.copy() #Dict kopyalama
print (ERPDict)
print(ERP.get('AX'))


# In[77]:


# copy() fonksiyonu
ERP = {"AX": "MS AXAPTA", "NAV" :"MS Navision", "SAP": "Systems Applications and Products"}
print
print (ERP)
print
print (ERP['AX'])
print (ERP['SAP'])
ERPDict=ERP.copy() #Dict kopyalama
print (ERPDict)
print
ERP["Odoo"]= "Odoo ERP Software" #dict veri yapısına üye ilave etme
print (ERP)
print (ERP.get("SAP", "not found")) #dict veri yapısında sorgu
print (ERP.get("ABC", "not found")) #dict veri yapısında sorgu


# In[79]:


ERP = {"AX": "MS AXAPTA", "NAV" :"MS Navision", "SAP": "Systems Applications and Products"}
print (ERP)
print
ERP["Odoo"]= "Odoo ERP Software" #dict veri yapısına üye ilave etme
print (ERP)
print (ERP.get("SAP", "not found"))#dict veri yapısında sorgu
print (ERP.setdefault('AX', "unknown")) #key ile sorgu 
print (ERP.setdefault('Dolibarr', "Dict veri yapısında mevcut değildir")) #key ile sorgu 
print (ERP)


# In[86]:


# in Sorguda True or False boolean sonuç döndürmektedir.

ERP = {"AX": "MS AXAPTA", "NAV" :"MS Navision", "SAP": "Systems Applications and Products"}
print (ERP)
print ("SAP"  in ERP) #dict veri yapısında sorgu
print ("Adempiere" in ERP) #dict veri yapısında sorgu


# In[89]:


#Dictionary veri yapısındaki key’leri listeler
ERP = {"AX": "MS AXAPTA", "NAV" :"MS Navision", "SAP": "Systems Applications and Products"}
print (ERP)
print

print (ERP.keys())

print (ERP.values())


# In[91]:


ERP = {"AX": "MS AXAPTA", "NAV" :"MS Navision", "SAP": "Systems Applications and Products"}
print (ERP)
print
ERP.items() # item() metodu
print (ERP.items())
#clear() metodu

ERP.clear()
print (ERP)


# In[92]:


dict = {'Marka': 'Toyota', 'Yıl': 2016}
print ("Marka : %s" %  dict.get('Yıl'))
print ("Value : %s" %  dict.get('Servis', "Mevcut Değil"))


# In[93]:


#HAFTA 5 - 6
#pandas kütüphanesi:

# versiyon belirleme
import pandas as pd
pd.__version__


# In[94]:


# install edilen kütüphaneler
pd.show_versions()


# In[96]:


#Python versiyon kontrol:

import sys
print(sys.version)


# In[97]:


#pandas veri yapısı olarak 2 yapı kullanılmaktadır:
#Series
#DataFrame
import pandas as pd
#seri = pd.Series([data], index=[index])
sayilar = pd.Series([0, 1, 4, 9, 16, 25, 36, 49], name='Sayi Kareleri')
print (sayilar)


# In[100]:


#index oluştruma
import pandas as pd

okyanus_derinlik= pd.Series([1205, 3646, 3741, 4080, 3270],index=['Kuzey Denizi',  'Atlas', 'Hint', 'Pasifik', 'Güney Okyanusu'])
print(okyanus_derinlik)


# In[101]:


#indeks ve dilimleme(Slicing)
import pandas as pd

okyanus_derinlik = pd.Series([1205, 3646, 3741, 4080, 3270], index=['Kuzey Denizi',  'Atlas', 'Hint', 'Pasifik', 'Güney Okyanusu'])
print (okyanus_derinlik)
print
print (okyanus_derinlik[2])
print
print (okyanus_derinlik[0:3]) #dilimleme işlemi
print
print (okyanus_derinlik['Pasifik'])
print
print (okyanus_derinlik['Atlas':'Pasifik'])#dilimleme işlemi


# In[102]:


#Dictionary ile Series deklarasyonu (tanımlaması)
# Dictionary ile Series deklarasyonu
import pandas as pd

okyanus_derinlik = pd.Series({
                    'Kuzey Denizi': 1205,
                    'Atlas': 3646,
                    'Hint': 3741,
                    'Pasifik': 4080,
                    'Güney Okyanusu': 3270
})

print (okyanus_derinlik)


# In[103]:


import pandas as pd

okyanus_derinlik = pd.Series({
                    'Kuzey Denizi': 1205,
                    'Atlas': 3646,
                    'Hint': 3741,
                    'Pasifik': 4080,
                    'Güney Okyanusu': 3270
})

print (okyanus_derinlik)
print

max_derinlik = pd.Series({
                    'Kuzey Denizi': 5567,
                    'Atlas': 8486,
                    'Hint': 7906,
                    'Pasifik': 10803,
                    'Güney Okyanusu': 7075
})

print (max_derinlik)


# In[105]:


#DATA FRAME yapısı

import pandas as pd

okyanus_derinlik = pd.Series({
                    'Kuzey Denizi': 1205,
                    'Atlas': 3646,
                    'Hint': 3741,
                    'Pasifik': 4080,
                    'Güney Okyanusu': 3270
})

print (okyanus_derinlik)
print(35*"-")

max_derinlik = pd.Series({
                    'Kuzey Denizi': 5567,
                    'Atlas': 8486,
                    'Hint': 7906,
                    'Pasifik': 10803,
                    'Güney Okyanusu': 7075
})
print
print(max_derinlik)
print(35*"-")

derinlikler = pd.DataFrame({
                    'ortalama Derinlik (metre)': okyanus_derinlik,
                    'Maksimum Derinlik (metre)':max_derinlik
})

print
print (derinlikler)


# In[106]:


#date_rage kullanımı
import pandas as pd

dates = pd.date_range('20170101', periods=14)

print (dates)


# In[107]:


import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("https://raw.githubusercontent.com/yew1eb/DM-Competition-Getting-Started/master/AV-loan-prediction/train.csv") #pandas kullanılarak veri setinin dataframe’e alınması
print (df.head(5))# veri seti başlangıcı ilk 5 veri listesi


# In[108]:


#describe() fonksiyonu ile veri setindeki nümerik alanlar incelebilir.

print (df.describe())


# In[109]:


#Nümerik olmayan alanların frekans dağılımı açısından analizi:

print (df['Property_Area'].value_counts())


# In[121]:


#Gelir Analizi Histogram diyagramı:

df['ApplicantIncome'].hist(bins=50)


# In[126]:


print (len(df)) #toplam veri sayısı
print (len(df.columns)) #toplam sütun sayısı


# In[131]:


#HAFTA 7-8
#DataFrame yapısının Series dictionary nesnesi ile oluşturulması: 
# stockSummaries bir dictionary'dir. Keyler 'AMZN' gibi stringler,  value'ları ise seridir. 
import pandas as pd
import numpy as np
# EPS hisse başına gelir
# Share outstanding ödenmemiş hisse
# Beta risk
# P/E Fiyat kazanç oranı
# Market cap şirketin değeri
stockSummaries={
'AMZN': pd.Series([346.15,0.59,459,0.52,589.8,158.88], 
        index=['Closing price','EPS',
                'Shares Outstanding(M)',
                'Beta', 'P/E','Market Cap(B)']),
'GOOG': pd.Series([1133.43,36.05,335.83,0.87,31.44,380.64],
        index=['Closing price','EPS','Shares Outstanding(M)',
               'Beta','P/E','Market Cap(B)']),
'FB': pd.Series([61.48,0.59,2450,104.93,150.92], 
      index=['Closing price','EPS','Shares Outstanding(M)',
             'P/E', 'Market Cap(B)']),
'YHOO': pd.Series([34.90,1.27,1010,27.48,0.66,35.36],
        index=['Closing price','EPS','Shares Outstanding(M)',
               'P/E','Beta', 'Market Cap(B)']),
'TWTR':pd.Series([65.25,-0.3,555.2,36.23],
       index=['Closing price','EPS','Shares Outstanding(M)',
              'Market Cap(B)']), 
'AAPL':pd.Series([501.53,40.32,892.45,12.44,447.59,0.84],
       index=['Closing price','EPS','Shares Outstanding(M)','P/E',
              'Market Cap(B)','Beta'])}
print (stockSummaries)
#print (stockSummaries['AMZN'])


# In[129]:


#Series DataFrame haline dönüşmesi
stockDF=pd.DataFrame(stockSummaries); 
print (stockDF)


# In[134]:


# DataFrame'nin csv dosyası olarak çalışılan klasörde kaydedilmesi
stockDF.to_csv('hisseSenediTest.csv')
kaydedilen = pd.read_csv('hisseSenediTest.csv')
print(kaydedilen)


# In[135]:


import pandas as pd
import numpy as np

veri = pd.read_csv('https://raw.githubusercontent.com/tdpetrou/Learn-Pandas/master/data/movie.csv')
print(35*"-")
print(veri.head())
print(35*"-")
print(veri.head(10))
print(35*"-")
print(veri.tail())
print(35*"-")
print(veri.tail(10))


# In[140]:


print (veri['director_name'])
print(35*"-")
print (veri.director_name)
print(35*"-")
print(35*"-")
#data set 'den iki farklı veri türünde iki farklı seri oluşturma
director = veri['director_name']
actor = veri['actor_1_facebook_likes']
print(35*"-")
print
print (director)
print(35*"-")
print (actor)


# In[138]:


# bütün name space import edildi
from math import *

factorial(5)


# In[139]:


# kütüphane m alias olarak import edildi
import math as m

m.factorial(5)


# In[ ]:




