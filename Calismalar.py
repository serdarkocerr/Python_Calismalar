#!/usr/bin/env python
# coding: utf-8

# In[2]:


#https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv
#1.Veri seti’ni pandas dataFrame ile okuyunuz.
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
print(df.head(5))


# In[61]:


#2.	DataFrame verileri ile ilgili özet bilgileri ekranda gösteriniz. # print(df.info())
print(df.info())


# In[4]:


#3.	pandas kütüphanesi versiyonu bulunuz.
pd.__version__


# In[5]:


#4.	İnstall edilen kütüphaneleri listeleyiniz.
pd.show_versions()


# In[6]:


#5.	Python Yazılımı Versiyonunu bulunuz
import sys
print (sys.version)


# In[62]:


#6.	Veri setindeki ilk 5 veriyi listeleyiniz.
print(df.head(5))


# In[63]:


#7.	Veri setindeki son 5 veriyi listeleyiniz
print(df.tail(5))


# In[47]:


#8.	Veri setindeki bütün verileri listeleyiniz.
print(df)


# In[64]:


#9.	Veri setindeki nümerik alanları listeleyiniz
print (df.describe())


# In[65]:


#10.Veri setindeki nümerik olmayan alanların frekans dağılımını analiz ediniz.
#Nümerik olmayan alanların frekans dağılımı açısından analizi:
print(35*'*' + ' NAME' + 35*'*')
print (df['NAME'].value_counts())
print(35*'*' + 'DEPARTMENT NAME ' + 35*'*')
print (df['DEPARTMENT NAME'].value_counts())
print(35*'*' + 'TITLE ' + 35*'*')
print (df['TITLE'].value_counts())
print(35*'*')

 


# In[4]:


#11.Histogram diyagramını çiziniz.

#df['REGULAR'].hist(bins=50)
df['DEPARTMENT NAME'].hist(bins=50)
#df['RETRO'].hist(bins=50)
#df['OTHER'].hist(bins=50)
#df['OVERTIME'].hist(bins=50)
#df['INJURED'].hist(bins=50)
#df['DETAIL'].hist(bins=50)
#df['QUINN/EDUCATION INCENTIVE'].hist(bins=50)
#df['TOTAL EARNINGS'].hist(bins=50)
#df['POSTAL'].hist(bins=50)


# In[89]:


#12.Veri setindeki toplam veri sayısını bulunuz.
print (len(df)) #toplam veri sayısı


# In[90]:


#13.	Veri setindeki toplam sütun sayısını bulunuz.
print (len(df.columns)) #toplam sütun sayısı


# In[91]:


#14.	Veri setindeki sütun isimlerini bulunuz.
for col in df.columns: 
    print(col) 


# In[55]:


#15.Veri setindeki eksik verileri bulunuz.
df1 = df[df.isna().any(axis=1)]
print(df1)


# In[48]:


#16.Her bir sütundaki eksik veri sayısını bulunuz.
df.isnull().sum()


# In[49]:


#17.	Bütün sütunlardaki toplam eksik veri sayısını bulunuz.
df.isnull().sum().sum()


# In[50]:


#18.	Eksik verilerin yerine ‘0 - sıfır’ yazınız.
import pandas as pd
import numpy as np
#1.yontem
#for col in df.columns:
#    df[col] = df[col].replace(np.nan, 0)
#2. yontem 
df.fillna(0)
#df.isnull().sum().sum()


# In[53]:


#19.	Eksik verileri dataFrame’den çıkarınız.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df = df.dropna()
#df.isnull().sum().sum()
print(df)


# In[113]:


#20.	Tekrarlı verilerin sayısını bulunuz.
duplicateRowsDF = df[df.duplicated()]
print("tekrarlı veriler:")
print(duplicateRowsDF)
print('tekrarli verileri sayisi : '  )
print(len(duplicateRowsDF))


# In[56]:


#21.	pandas_profiling kütüphanesini kullanarak dataFrame’deki veriler hakkında “html” rapor hazırlayınız.
import pandas_profiling
import pandas as pd
#pandas_profiling.ProfileReport(df)
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.profile_report()


# In[57]:


#22.	CSV dosyası olarak link’ten alınan dataFrame’i herhangi bir dizine dataFrame olarak kopyalayınız. Linkteki CSV dosyası ile kaydedilen CSV dosyasının aynı olup olmadığını kontrol ediniz.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması

df.to_csv (r'C:\Users\Serdar\Desktop\Yuksek Lisans\Dönem-2\phyton\odev1\test.csv', index = False, header=True)

A=set(pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv", index_col=False, header=None)[0]) #reads the csv, takes only the first column and creates a set out of it.
B=set(pd.read_csv("C:/Users/Serdar/Desktop/Yuksek Lisans/Dönem-2/phyton/odev1/test.csv", index_col=False, header=None)[0]) #same here
print(A-B) #set A - set B gives back everything thats only in A.
print(B-A) # same here, other way around.


# In[14]:


#23.	DataFrame’ki herhangi bir sütunu ekrana alınız ve veri tipini sorgulayınız.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
print(df.POSTAL)
dataTypeSeries = df.dtypes['POSTAL']
 
print('Data type of each column of Dataframe  POSTAL :')
print(dataTypeSeries)


# In[58]:


#24.	Sütunun class’ını sorgulayınız.
print (df['POSTAL'].apply(type))


# In[59]:


#25.	DataFrame’de “loc  “ deyimi kullanarak indeks etiketi ile sorgu yapınız.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması

#a.) Selecting rows by label/index --> df.set_index()
#Selections using the loc method are based on the index of the data frame (if any).
#.loc method directly selects based on index values of any rows.
#NAME'i set ediyoruz.  NAME kolunundan istediğimiz index'i alabiliyoruz. 
df.set_index("NAME", inplace=True)
#df.loc['Miller,Francis T']
df.loc[['Miller,Francis T','Connolly,John J']]
df.loc[['Miller,Francis T','Connolly,John J'], 'DEPARTMENT NAME':'TITLE']
df.loc['Miller,Francis T':'Connolly,John J', ['DEPARTMENT NAME','TITLE']]

#2b. Boolean / Logical indexing using .loc--> data.loc[<selection>]
#herhangi bir set işlemi yapmıyoruz.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
# Select rows with  NAME  Miller,Francis T, # and all columns between 'DEPARTMENT NAME' and 'RETRO'
df.loc[df['NAME'] == 'Miller,Francis T', 'DEPARTMENT NAME':'RETRO']



# In[26]:


#26.	DataFrame’de “iloc  “ deyimi kullanarak indeks numarası ile sorgu yapınız.
# integer-location based indexing / selection by position.
#There are two “arguments” to iloc – a row selector, and a column selector.

# Rows:
df.iloc[0] # first row of data frame
df.iloc[0:5] # first five rows of dataframe
# Columns:
df.iloc[:,0] #first column of data frame 
df.iloc[:, 0:2] # first two columns of data frame with all rows

df.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
df.iloc[0:5, 5:8] # first 5 rows and 5th, 6th, 7th columns of data frame 


# In[60]:


#27.	Satır ve sütunu birlikte seçerek “loc” deyimi ile sorgu yazınız.
#1.yöntem
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.set_index("NAME", inplace=True)
df.loc[['Miller,Francis T','Connolly,John J'], ['DEPARTMENT NAME','TITLE']]

#2.yöntem
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.loc[df['NAME'] == 'Miller,Francis T', ['DEPARTMENT NAME','TITLE']]


# In[61]:


#28.	loc () deyimini kullanarak dataFrame’de “Slicing” işlemi yapınız.
#1.yöntem
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.set_index("NAME", inplace=True)
df.loc['Miller,Francis T':'Connolly,John J', 'DEPARTMENT NAME':'TITLE']

#2.yöntem
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.loc[df['NAME'] == 'Miller,Francis T', ['DEPARTMENT NAME','TITLE']]


# In[83]:


#29.	DataFrame’de filtreleme işlemi yapınız.

df[(df['NAME'] == 'Miller,Francis T') & (df['DEPARTMENT NAME'] == 'Boston Police Department')]
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması

#Query ile filtreleme
df.query('TITLE=="Police Lieutenant (Det)"')

#filter ile filtreleme
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.filter(items=['RETRO', 'DEPARTMENT NAME'])


# In[84]:


#30.	DataFrame’de indeksi sıfırlayınız.
#reset_index() to reset pandas index to zero --> We can reset the row index in pandas with reset_index() to make the index start from 0.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması

df.reset_index()


# In[88]:


#31.	dataFrame’e yeni bir sütun ilave ediniz
import numpy as np
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df["TestColumn"] =  np.nan
print(df)


# In[90]:


#32.	DataFrame’den bir sütunu geçici olarak siliniz.
#drop fonksiyonu dataframe'den kolunu silinmiş bir dataframe döndürür. Gerçek dataframe'den silmez. 
#Çünkü defaultta inplace parametresi False'tır.
#axis 0 = row , 1 = column

df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
dfdropped = df.drop(['NAME'] ,axis = 1)
print(dfdropped)
print(df)


# In[92]:


#33.	DataFrame’den bir sütunu kalıcı olarak siliniz.
#1.yontem inplace = True yapılır.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.drop(['NAME'] ,axis = 1, inplace = True )
print(df)
#2.yontem inplace = False iken yani defaultta iken sonucu yeniden df ye atamak.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df = df.drop(['NAME'] ,axis = 1)
print(df)


# In[93]:


#34.	DataFrame hakkında genel bilgiyi ekranda listeleyiniz
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.info()


# In[94]:


#35.	System Kütüphanesi versiyonunu bulunuz
import sys
print (sys.version)


# In[95]:


#36.	Pandas Kütüphanesi versiyonunu bulunuz.
import pandas as pd
pd.__version__


# In[98]:


#37.	Matplotlib kütüphanesi versiyonunu bulunuz.
import matplotlib
matplotlib.__version__


# In[100]:


#38.	Keras kütüphanesi versiyonunu bulunuz.
import keras
keras.__version__


# In[62]:


#39.	“pd.pivot.table()” metodunu kullanarak, dataFrame’deki bir sütundan tek indeksli “pivot table” oluşturunuz.
# pivot tablo -> daha anlaşılır bir biçimde ve özet halinde sunulması
import locale
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
#print(df)
pd.pivot_table(df, values='POSTAL',index=['DEPARTMENT NAME'],columns='TITLE',aggfunc=[min])


# In[63]:


#40.	“pd.pivot.table()” metodunu kullanarak, dataFrame’deki birden fazla sütundan çok indeksli “pivot table” oluşturunuz.
import locale
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
pd.pivot_table(df, values='POSTAL',index=['DEPARTMENT NAME','NAME'],columns='TITLE',aggfunc=[min])


# In[130]:


#41.	Pivot_table’da “aggfunc=np.sum” gonksiyonunu kullanınız.

df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
pd.pivot_table(df, values='POSTAL',index=['DEPARTMENT NAME','NAME'],columns='TITLE',aggfunc=np.sum)


# In[64]:


#42.	dataFrame’i CSV dosyası olarak kaydediniz.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.to_csv (r'C:\Users\Serdar\Desktop\Yuksek Lisans\Dönem-2\phyton\odev1\test.csv', index = False, header=True)


# In[65]:


#43.	dataFrame’i excel dosyası olarak kaydediniz.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.to_excel(r'C:\Users\Serdar\Desktop\Yuksek Lisans\Dönem-2\phyton\odev1\test.xlsx', sheet_name='dftoexcelTest', index = False)


# In[66]:


#44.	dataFrame’i html dosyası olarak kaydediniz.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.to_html(open(r'C:\Users\Serdar\Desktop\Yuksek Lisans\Dönem-2\phyton\odev1\test.html', 'w'))


# In[135]:


#45.	dataFrame’i JSON dosyası olarak kaydediniz.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.to_json(r'C:\Users\Serdar\Desktop\Yuksek Lisans\Dönem-2\phyton\odev1\test.json')


# In[137]:


#46.	dataFrame’i txt dosya olarak kaydediniz.
import numpy as np
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df.to_csv(r'C:\Users\Serdar\Desktop\Yuksek Lisans\Dönem-2\phyton\odev1\test.txt', header=None, index=None, sep=' ', mode='a')


# In[169]:


#47.	dataFrame’deki bir sütunu küçükten büyüğe sıralayınız.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df['NAME'].sort_values(ascending=True)


# In[170]:


#48.	dataFrame’deki bir sütunu büyükten küçüğe sıralayınız.
df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması
df['NAME'].sort_values(ascending=False)


# In[172]:


#49.	dataFrame’deki iki sütunu küçükten büyüğe sıralayınız.

df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması

df[['NAME', 'DEPARTMENT NAME']].sort_values(by=['NAME', 'DEPARTMENT NAME'],ascending=[True,False])


# In[173]:


#50.	dataFrame’deki iki sütunu büyükten küçüğe sıralayınız.

df = pd.read_csv("https://raw.githubusercontent.com/Turanga1/Boston-Earnings-Analysis/master/employee-earnings-report-2017.csv") #pandas kullanılarak veri setinin dataframe’e alınması

df[['NAME', 'DEPARTMENT NAME']].sort_values(by=['NAME', 'DEPARTMENT NAME'],ascending=[False,False])


# In[ ]:




