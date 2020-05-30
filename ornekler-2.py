#!/usr/bin/env python
# coding: utf-8

# In[72]:



#pandas, Python programlama dili için geliştirilen 
#açık kaynak kodlu bir veri analizi kütüphanesidir.

#Series
#pandas veri yapılarından birisi olan Series, 
#değişik veri türlerinden aynı veri türünü saklayabilen 
#tek boyutlu bir vektör veya bir dizidir. 


'''
DataFrame satır ve sütunlardan oluşan bir tablodur. 
DataFrame’deki her bir sütun Series nesnesidir. 
Satırlarda ise Series’nin elemanları(veriler) yer alır. 
DataFrame, built-in Python dictionary kullanılarak oluşturulabilir.

Dataframe içindeki dictionary'lerin keyleri kolon isimleri,
value'lar ise serilerdir.  Yani her kolon aslında bir seridir.
Serilerin indexleride  de
dataframe tablosundaki rowlardır. Veya Serilerde dictionary'den oluştuğunu düşünürsek serilerin 
keyleri rowlardır.
Default indexler 0...N-1'dir.

'''
#dataframe serilerinin indexleri  tektir yani aynıdır. Bu sebepten eğer dictionaryden oluşursa
#keyler her seri için aynı olmalıdır.
#eğer dict olarak oluşturulmamışsa default 0...N-1 verilir.


# In[71]:


#HAFTA 10
get_ipython().run_line_magic('config', 'IPCompleter.greedy=True # Intellisense için koyulur. tab ile çalışır')
#Series Kullanımı
import pandas as pd
sayilar = pd.Series([0, 1, 5, 6, 7, 8, 90, 104, 9, 160, 250, 46, 19], name='Sayilar ')
print (sayilar)


# In[9]:


#DataFrame
#CSV dosyasından veri okuma
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/QuantLet/MVA/master/QID-1226-MVAportfol/apple.csv', index_col='Date',parse_dates=True) #Tarih date olarak belirlendi
df = df.sort_index()
print(df.info()) # veriler ile ilgili özet bilgi


# In[17]:


#indexi biz belirtiyoruz. Belirtmezsek default 0,1,2,3... olarak gelir. 
# Date olarak belirttik ve bu Date kolonu dataframe içinde mevcut olmalıdır.
import pandas as pd
df= pd.read_csv('https://raw.githubusercontent.com/QuantLet/MVA/master/QID-1226-MVAportfol/apple.csv', index_col='Date',parse_dates=True) #Tarih dateolarak belirlendi
df1= pd.read_csv('https://raw.githubusercontent.com/QuantLet/MVA/master/QID-1226-MVAportfol/apple.csv')

df= df.sort_index()
print(df) # veriler ile ilgili özet bilgi
print(df1)
print(df.info()) # veriler ile ilgili özet bilgi


# In[20]:


#2009 yılı hisse senedi kapanış fiyat ortalaması
df.loc['2009', 'Close'].mean()#satır sütün gibi.


# In[21]:


print ('dörtyillikortalamakapanışfiyatı:')
print (df.loc['1999-Jan':'2009-Jan', 'Close'].mean())


# In[33]:


import pandas as pd
#loc, dizinden belirli labels ile satır (veya sütun) alır. iloc index'e göre alır.
#loc verileri yalnızca etiketlerle seçer
#iloc, dizinde belirli konumlar değerinde satır (veya sütun) alır (bu nedenle yalnızca tamsayılar alır).
#satırlar index'ler sütünlar ise dictionary keyleri.(age,color,food,height,score,state)
dftest = pd.DataFrame({'age':[30, 2, 12, 4, 32, 33, 69],
                   'color':['blue', 'green', 'red', 'white', 'gray', 'black', 'red'],
                   'food':['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese', 'Melon', 'Beans'],
                   'height':[165, 70, 120, 80, 180, 172, 150],
                   'score':[4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'state':['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean', 'Christina', 'Cornelia'])

dftest.loc[['Cornelia', 'Jane', 'Dean']] # 'Cornelia', 'Jane', 'Dean' indexlerine denk gelen bütün kolonları alır.
dftest.loc['Aaron':'Dean'] # 'Aaron' dan 'Dean'e(dahil) bütün indexlere denk gelen bütün kolonları alır.
dftest.loc[['Jane', 'Dean'], 'color'] #Jane ce Dean indexine denk gelen color kolonunun verilerini alır.
dftest.loc[['Jane', 'Dean'], 'height':] # Jane ve Dean indexine denk gelen height kolonundan state kolonuna kadar verilerini alır.

dftest.iloc[4] # 4. satıra denk gelen bütün sütunları al.(index 4-> 0,1,2,3,4 )
dftest.iloc[[1,4], 2] # 1. ve 4. satırdaki 2. sütün değerini döndürür.

#print(dftest.loc[['Cornelia', 'Jane', 'Dean']])
#print(dftest.loc['Aaron':'Dean'])
print(dftest.loc[['Jane', 'Dean'], 'color'])
#print(dftest.loc[['Jane', 'Dean'], 'height':])

#print(dftest.iloc[4])
print(dftest.iloc[[1,4], 2])


# In[35]:


#matplotlib: Çeşitliformatlardagrafik çizmek için kullanılan Python 2Dçizimkütüphanesi
# yıllara göre kapanış grafik, veri görselleştirme
import matplotlib.pyplot as plt

data_frame= df.loc['2005-Jan':'2014-Jan', ['Close']]
data_frame.plot()
plt.show()


# In[52]:


import pandas as pd
#Web Sitesinden CSVdosyasının okunması
df=pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
#df= pd.read_csv("Salaries.csv")# CSV dosyasını çalışılan klasörden okuma
#İlk 5 verininListesi
print (df.head())# ilk 5 veri veya
print
print (df.head(5)) # ilk 5 veri


# In[37]:


# ilk 15 verinin listesi
print (df.head(15))


# In[38]:


#Son 5 Observation-VeriListesi
print
print(df.tail(5))


# In[39]:


# Bütün observation-kayıtlarınlistesi
# tail(-1) 0 . index olmuyor sonucta
#bütün kayıt için df print edilmeli sadece.
print
print(df.tail(-1))


# In[40]:


#sütun veri türünün incelenmesi
print
print (df.dtypes)


# In[41]:


print (df.columns) # dataFramesütun isimleri


# In[42]:


#satır etiketleri ve sütun isimleri
#satır etiketleri index 0 dan başlıyor.
print (df.axes)


# In[43]:


# dataframe’dekitoplam veri sayısı
print
print(df.size) # dataFrameveri sayısı


# In[44]:


#dataFrame sayısal alanlar için temel istatistikler
print
print(df.describe())


# In[45]:


# maksimum veri
print
print(df.max())


# In[46]:


# En düşük veri
print
print(df.min())


# In[47]:


#HAFTA 11
print() # ortalama kayıt
print (df.mean())


# In[48]:


# medyan ortanca değer
print
print (df.median())


# In[49]:


#standart sapma
print
print (df.std())


# In[50]:


#metadata
df.info()


# In[65]:


#Unvan kullanılarak veri guruplama
#SQL sorgusu gibidir. Gruplamadan sonra grup fonksiyonu olan ortalama ifadesi kullanılırsa anlamlı olur.
df_Unvan = df.groupby(['rank'])
print (df_Unvan.head(5))
print(35*'-')
print (df_Unvan.mean())# gruplama sonucunda sayısal alanların ortalaması


# In[68]:


# dataframe’deki toplam veri sayısı
import pandas as pd
flights = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/flights.csv")
print
print (flights.size) # dataFrame toplam veri sadyısı
print (flights.info()) # dataFrame metadata 


# In[69]:


#Bir observationda bir veri mevcut değil ise ekrana getir – missing data’nın bulunması
print (flights[flights.isnull().any(axis=1)].head())


# In[70]:


#Bir observationda bir veri mevcut değil ise ekrana getir – missing data’nın bulunması
#flights.isnull() ifadesi  her satırın her sütünuna bakarak NaN var mı diye kontrol ederek o field için true/false yazan df döndürür.
#axis = 1 -> satırda hiç nan var mı diye bakar ve satır için true/false ifadesi döndürür.
# flights dataframe için [] ifadesi içinde yazılırsa sadece true olan satırları getirir. Yani NaN olanları.
print (flights[flights.isnull().any(axis=1)].head())
print (flights.isnull())
print (flights.isnull().any(axis=1))


# In[ ]:


######### Sunum 8  ################


# In[73]:


import pandas as pd 

df = pd.DataFrame({
     'ulke': ['Kazakistan', 'Romanya', 'Polonya', 'Ukrayna'],
     'nufus': [17.04, 19.6, 38.1, 45.5],
     'yuzolcum': [2724902, 230170, 312679, 603628]
 })
print (df)


# In[74]:


print
print (df['ulke'])
print
# her bir sütun bir Series nesnesidir
print (type(df['ulke']))


# In[75]:


# multiple line remainder
#DataFrame nesnesinin 2 indeksi vardır: sütun indeksi ve satır indeksi. 
#satır indeksi belirtilmemiş ise, pandas RangeIndex oluşturur. range 0 - N-1’e kadardır. 
#N ise DataFrame'deki satır sayısıdır.


print
print (df.columns)
print
print (df.index)


# In[76]:


df = pd.DataFrame({
     'ulke': ['Kazakistan', 'Romanya', 'Polonya', 'Ukrayna'],
     'nufus': [17.04, 19.6, 38.1, 45.5],
     'yuzolcum': [2724902, 230170, 312679, 603628]
 }, index=['KZ', 'RO', 'PL', 'UA'] )
print (df)


# In[77]:


#İndeks ismi ilave edilirse:
print
df.index = ['KZ', 'RO', 'PL', 'UA']
df.index.name = 'Ulke Kodları'
print (df)


# In[78]:


#Series nesnesi indeksi  DataFrame indeksi gibidir:
print
print (df['ulke'])


# In[79]:


''' ILOC ve LOC
İndeks kullanılarak satırlara erişim şu şekilde yapılabilir:
.loc ve indeks etiketi ile
.iloc ve indeks numarası ile
'''
print
print (df.loc['KZ']) #indeks etiketi(label)
print("-------")
print (df.iloc[0]) #indeks numarası


# In[80]:


#satır ve sütunun birlikte seçilmesi:
print
print (df.loc[['KZ', 'RO'], 'nufus'])#--> nufus sütun


# In[81]:


#.loc 2 argüman alır: indeks list ve sütun list, dilimleme(slicing operation) yapılabilir:

print
print (df.loc['KZ':'PL', :])#KZ den PL ye kadar PL dahil satırlar, : bütün sütünlar.


# In[82]:


#Filtreleme işlemi(Filtering) yapılabilir:

print
print (df[df.nufus > 20][['ulke', 'yuzolcum']])# nufus>20 den fazla olarak dataframe'i tekrar düzenleyip, bu df'den ulke ve yuzolcum serilerini getir.


# In[83]:


# dataFrame’deki sütunlar, özellik(attribute) ile veya Python dictionary notasyonu ile erişilebilir.
print
print (df.nufus) 
print
print (df['nufus'])


# In[85]:


#indeks resetlenebilir
#resetlenince 0..N-1 şeklinde olur.Tabi orjinali değiştirmez orjinali değiştirmek için df=df.reset_index() yapılmalı.
print
print (df.reset_index())
print (df)


# In[86]:


# dataFrame’e yeni bir sütun ilave edilebilir
# nüfus yoğunluğu sütunu ilavesi
print
df['yogunluk'] = df['nufus'] / df['yuzolcum'] * 1000000
print (df)


# In[87]:


# dataFrame’de sütun geçici olarak silinebilir:
print
print (df.drop(['yogunluk'], axis='columns'))
print (df)


# In[88]:


#sütunun tamamen silinmesi için del df[‘yogunluk’]

print
del df['yogunluk']
print (df)


# In[ ]:


# HAFTA 12-14 


# In[90]:


# random sayı üretmek için numpy kullanılır.
#tesadüfü sayılar için 
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

#titanic_df = pd.read_csv('train_Titanic.csv')
titanic_df = pd.read_csv("https://raw.githubusercontent.com/felipegonzalez/aprendizaje_estadistico_2015/master/clases/clase_12/datos/train_titanic.csv")
print (titanic_df.head())


# In[91]:


#DataFrame’deki ilk 15 verinin listesi:
print (titanic_df.head(15))


# In[92]:


#DataFrame’deki son 5 verinin listesi:
print (titanic_df.tail(5))


# In[94]:


#Dataset hakkında genel bilgi için:
print
print (titanic_df.info())


# In[96]:


#Hayatta kalanlar için grafik çizimi
print (sns.factorplot('Sex', data=titanic_df,kind='count'))


# In[100]:


# Yolcuların mevkilere göre dağılımı ve mevkilerdeki cinsiyet'e göre gösterimi(hue).
sns.factorplot('Pclass',data=titanic_df,hue='Sex',kind='count')


# In[102]:


#ERP şirket pazar payları
#pyplot
#pyplot modülü, matplotlib’nin MATLAB gibi kullanılmasını sağlayan fonksiyonlardan oluşmaktadır.

import matplotlib.pyplot as plt
ERP = ['Infor','Oracle','SAP','Axapta']
pazar_payi = [10,30,45,15]
colors = ['yellow','green','red','blue']
plt.pie(pazar_payi, labels=ERP, colors=colors)
plt.axis('equal')


# In[103]:


#import matplotlib.pyplot as plt
# x ekseni index'e göre
# y ekseni ise seri value'lara göre oluşuyor.
import pandas as pd
data = {'series1':[1,3,4,3,5,6],
            'series2':[2,4,5,2,4,3],
            'series3':[3,2,3,1,3,4]}
df = pd.DataFrame(data)
df.plot(kind='bar') # çubuk diyagram çizilmesi


# In[104]:


import pandas as pd
from IPython.display import display

# data set oluşturulması
data = {'isim': ["Kaya", "meltem", "temel", "bekir"],
        'sehir' : ["izmir", "istanbul", "ordu", "ankara"],
        'yas' : [47, 73, 53, 33]
       }

data_pandas = pd.DataFrame(data)
display(data_pandas)


# In[105]:


import pandas as pd
from IPython.display import display
print
#query-sorgu
#40 yaşından büyük olan kişilerin listesi
# filtreleme
display(data_pandas[data_pandas.yas > 40])


# In[106]:


print
import sys
print("Python version: {}".format(sys.version))

import pandas as pd
print("pandas version: {}".format(pd.__version__))

import matplotlib
print("matplotlib version: {}".format(matplotlib.__version__))


# In[109]:


# URL'den sayfayı okuyup parse edebiliyor.
#import urllib.request 
from lxml import html

url = "http://www.infolanka.com/miyuru_gee/art/art.html"
page = html.fromstring(urllib.request.urlopen(url).read())

for link in page.xpath("//a"):
    print ("Name", link.text, "URL", link.get("href"))


# In[112]:


#Pandas ile de html den veri alınabilir. Okunan tabloda ilk row'un yani 0. row'un header olduğunu belirtirsek
#pandas bunu kolon isimleri olarak alır.
import pandas as pd

url='http://floodobservatory.colorado.edu/Version3/MasterListrev.htm'
veri=pd.read_html(url, header=0)

print (veri[0])


# In[113]:


#bitki dataseti
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv')

print(df.head())


# In[114]:


#scatter grafik.
# create a figure and axis
fig, ax = plt.subplots()

# scatter the sepal_length against the sepal_width
ax.scatter(df['sepal_length'], df['sepal_width'])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')


# In[115]:


# create color dictionary
colors = {'setosa':'r', 'versicolor':'g', 'virginica':'b'}

# create a figure and axis
fig, ax = plt.subplots()

# plot each data-point
for i in range(len(df['sepal_length'])):
    ax.scatter(df['sepal_length'][i], df['sepal_width'][i], color=colors[df['species'][i]])

# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')


# In[117]:


#keras --> deep learning kütüphanesidir. CPU ve GPU çalışır.
import keras
keras.__version__


# In[118]:


######## 9. SLAYT  #####################


# In[119]:


# bir okulun veri seti.
#kütüphanelerin deklarasyonu
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
sns.set(font_scale=1.5)


# In[120]:


# veri setinin GitHub’tan alınması
df= pd.read_csv('https://raw.githubusercontent.com/LearnDataSci/article-resources/master/Essential%20Statistics/middle_tn_schools.csv')


# In[121]:


# dataframe'inekranda gösterilmesi
print(df)


# In[122]:


# sütun indeksleri
print
print(df.columns)


# In[123]:


#indexler
#Toplam veri satırı sayısı 347
print
print(df.index)


# In[124]:


# school_rating sütunu incelenmesi
print
print (df['school_rating'])


# In[125]:


# indeks numarası ile verinin listesi
print
print(df.iloc[342]) #indeksnumarası


# In[126]:


#Filtreleme işlemi(Filtering):
print
print(df[df.school_rating> 3][['name', 'school_type']])


# In[127]:


#Filtreleme işlemi(Filtering):
print
print(df[df.school_rating>= 4][['school_rating','name', 'school_type']])


# In[128]:


# DataFrame’dekiilk 5 verinin listesi
print(df.head())


# In[129]:


# DataFrame’dekison 5 verinin listesi:
print(df.tail())


# In[130]:


# Datasethakkında genel bir bilgi
print
print(df.info())


# In[131]:


# genel istatistkbilgi
df.describe()


# In[132]:


#Pandas groupby methodu
# school_rating değerlerindeki reduced_launch'ların sayısı, ortlaması vs.
df[['reduced_lunch', 'school_rating']].groupby(['school_rating']).describe()


# In[133]:


# 2 sütundaki veri arasındaki korelasyonun bulunması
df[['reduced_lunch', 'school_rating']].corr()


# In[134]:


#Veri seti grafikleri:
#Box-and-Whisker Plot ortalamadan uzaklığı göstermektedir.
fig, ax= plt.subplots(figsize=(14,8))
ax.set_ylabel('school_rating')
# boxplot with only these two variables
_ = df[['reduced_lunch', 'school_rating']].boxplot(by='school_rating', figsize=(13,8), vert=False, sym='b.', ax=ax)


# In[ ]:


#14. Hafta Python 014 sunusu# 

# genel olarak matplotlibrary'i kullanıyoruz.
# Daha hassas grefikler için seaborn 
#‘%matplotlibinline’ komutu JupyterNotebook’ta grafik gösterilmesinin kolaylaştırılması için kullanılır.


# In[138]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sıcaklık= [14.2, 16.4, 11.9, 12.5, 18.9, 22.1, 19.4, 23.1, 25.4, 18.1,22.6, 17.2]
satış= [215.20, 325.00, 185.20, 330.20, 418.60, 520.25, 412.20, 614.60,544.80, 421.40, 445.50, 408.10]

#scatter plot’un çizimi–kırmızı renk
plt.scatter(sıcaklık, satış, color='red')# x:sıcaklık, y: satış
#plt.scatter(sıcaklık, satış, color=‘blue')
plt.show()


# In[137]:


plt.title('Satış Miktarı ve Sıcaklık')
plt.ylabel('Satış')
plt.xlabel('Sıcaklık')
plt.scatter(sıcaklık, satış, color='brown')
plt.show()


# In[139]:


#LineChart Çizimi:
hisse_fiyatı= [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45,196.42, 200.32, 200.32, 200.85, 199.2, 199.2, 199.2, 199.46, 201.46,197.54, 201.12, 203.12, 203.12, 203.12, 202.83, 202.83, 203.36, 206.83,204.9, 204.9, 204.9, 204.4, 204.06]
import matplotlib.pyplot as plt
plt.plot(hisse_fiyatı)
plt.title('Hisse Fiyatı')
plt.xlabel('Gün')
plt.ylabel('TL')
plt.show()


# In[140]:


# günleri birinci günden başlatmak ve haftalık günlerin belirtilmesi
t = list(range(1, 31))
plt.title('Hisse Fiyatı')
plt.xlabel('Gün')
plt.ylabel(' TL ')
plt.plot(t, hisse_fiyatı, marker='.', color='red')
plt.xticks([1, 8, 15, 22, 28])
plt.show()


# In[141]:


# Bar PlotÇizilmesi
notlar = ['AA','BA','BB','CB','CC','DC','DD','FD','FF']
öğrenciSayısı= [10, 15, 25, 10, 5, 8, 12, 4, 3]
import matplotlib.pyplot as plt
plt.bar(notlar, öğrenciSayısı, color=['green', 'gray', 'green', 'gray', 'gray', 'red', 'yellow', 'brown', 'blue'])


# In[ ]:




