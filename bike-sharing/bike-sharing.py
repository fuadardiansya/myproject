#!/usr/bin/env python
# coding: utf-8

# # PROYEK DATA ANALIS - BIKE SHARING DATAFRAME

# * Nama  : Fuad Hidayat Ardiansya
# * Email : f.h.ardiansya@gmail.com

# ### MENENTUKAN PERTANYAAN BISNIS

# * 1. Bagaimana intensitas jumlah sewa sepeda harian setiap musim(season)?
# * 2. Bagaimana intensitas jumlah sewa sepeda harian setiap tahun(year)?
# * 3. Bagaimana intensitas jumlah sewa sepeda harian setiap bulan(month)?
# * 4. Bagaimana dampak cuaca(weathersit) terhadap jumlah sewa sepeda harian?
# * 5. Bagaimana perbedaan jumlah sepeda harian antara hari kerja(workingday) dan hari libur(holiday)?

# ### MENYIAPKAN SEMUA LIBRARY YANG DIBUTUHKAN

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# ## DATA WRANGLING

# ### GATHERING DATA

# In[2]:


#Membaca dataset
days_df = pd.read_csv("https://raw.githubusercontent.com/fuadardiansya/streamlit-bike-sharing/main/day.csv")


# In[3]:


#Menampilkan dataset
days_df.head()


# In[4]:


hours_df = pd.read_csv("https://raw.githubusercontent.com/fuadardiansya/streamlit-bike-sharing/main/hour.csv")


# In[5]:


hours_df.head()


# In[6]:


#Menghitung jumlah dataframe
print("Jumlah dataframe day:", days_df.shape[0])
print("Jumlah dataframe hour:", hours_df.shape[0])


# In[7]:


#Mengabungkan dataframe
days_hours_df = days_df.merge(hours_df, on='dteday', how='inner', suffixes=('_daily','_hourly'))
print(days_hours_df.shape)
#Menampilkan hasil penggabungan dataframe
days_hours_df.loc[days_hours_df["dteday"].isnull()]
days_hours_df.head()


# ### ASSESSING DATA

# In[8]:


#Memeriksa dataframe days_df
days_df.info()


# In[9]:


#Memeriksa dataframe hours_df
hours_df.info()


# In[10]:


#Memeriksa dataframe days_hours_df
days_hours_df.info()


# In[11]:


#Memeriksa jumlah missing values days_df
days_df.isna().sum()


# In[12]:


#Memeriksa jumlah missing values hours_df
hours_df.isna().sum()


# In[13]:


#Memeriksa jumlah missing values days_hours_df
days_hours_df.isna().sum()


# In[14]:


print("Jumlah duplikat: ", days_df.duplicated().sum())
print("Jumlah duplikat: ", hours_df.duplicated().sum())
print("Jumlah duplikat: ", days_hours_df.duplicated().sum())


# In[15]:


#Menampilkan ringkasan dataframe days_df
days_df.describe()


# In[16]:


#Menampilkan ringkasan dataframe hours_df
hours_df.describe()


# In[17]:


#Menampilkan ringkasan dataframe days_hours_df
days_hours_df.describe()


# ### CLEANING DATA

# In[18]:


#Tidak terdapat data duplikat dan missing value


# ## EXPLORATORY DATA ANALYSIS (EDA)

# In[19]:


#Mendefinisikan fungsi yang akan digunakan
def range(series):
    return series.max() - series.min()


# In[20]:


days_hours_df.describe(include="all")


# In[21]:


days_hours_df.groupby(by="season_hourly").agg({
    "workingday_hourly": "count", #Menjumlahkan penyewa pada hari kerja berdasarkan musim
    "windspeed_hourly": ["max", "min", "mean", lambda x: x.max() - x.min()] #Membuat fungsi kustom untuk range
}).sort_values(by=("workingday_hourly", "count"), ascending=False)


# In[22]:


days_hours_df.groupby(by="season_daily").agg({
    "workingday_hourly": "count", #Menjumlahkan penyewa pada hari kerja berdasarkan musim
    "windspeed_hourly": ["max", "min", "mean", lambda x: x.max() - x.min()] #Membuat fungsi kustom untuk range
}).sort_values(by=("workingday_hourly", "count"), ascending=False)


# In[23]:


days_hours_df.groupby(by="season_daily").mnth_daily.nunique().sort_values(ascending=False)


# In[24]:


days_hours_df.groupby(by="season_daily").instant_daily.nunique().sort_values(ascending=False)


# In[25]:


days_hours_df.groupby(by="season_daily").cnt_daily.nunique().sort_values(ascending=False)


# In[26]:


days_hours_df.groupby(by="season_daily").cnt_hourly.nunique().sort_values(ascending=False)


# In[27]:


days_hours_df.groupby(by="weathersit_daily").cnt_daily.nunique().sort_values(ascending=False)


# In[28]:


days_hours_df.groupby(by="weathersit_daily").cnt_hourly.nunique().sort_values(ascending=False)


# In[29]:


days_hours_df.groupby(by="mnth_daily").cnt_daily.nunique().sort_values(ascending=False)


# In[30]:


days_hours_df.groupby(by="mnth_daily").cnt_hourly.nunique().sort_values(ascending=False)


# In[31]:


#Mencari Value Korelasi Setiap Data perhari
numerical_columns = ["holiday_daily","weekday_daily","workingday_daily","weathersit_daily","temp_daily","atemp_daily","season_daily", "windspeed_daily",  "cnt_daily"]
correlation = days_hours_df[numerical_columns].corr()
print(correlation)


# ## Visulization & Explanatory Analysis

# ### 1. Bagaimana intensitas jumlah sewa sepeda harian setiap musim(season)?

# In[32]:


data_musimku = days_hours_df.groupby("season_daily")["cnt_daily"].mean()
jenis_musim = ["Springer","Summer","Fall", "Winter"]
plt.figure(figsize=(10, 5))
plt.bar(jenis_musim, data_musimku)
plt.title("INTENSITAS JUMLAH SEWA SEPEDA HARIAN SETIAP MUSIM")
plt.xlabel("Season")
plt.ylabel("Rata-Rata Jumlah Sewa Sepeda Harian")
plt.show()


# ### 2. Bagaimana intensitas jumlah sewa sepeda harian setiap tahun(year)?

# In[33]:


data_tahunku = days_hours_df.groupby("yr_daily")["cnt_daily"].mean()
jenis_tahun = ["2011","2012"]
plt.figure(figsize=(10, 5))
plt.bar(jenis_tahun, data_tahunku)
plt.title("INTENSITAS JUMLAH SEWA SEPEDA HARIAN SETIAP TAHUN")
plt.xlabel("Season")
plt.ylabel("Rata-Rata Jumlah Sewa Sepeda Harian")
plt.show()


# ### 3. Bagaimana intensitas jumlah sewa sepeda harian setiap bulan(month)?

# In[34]:


fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="mnth_daily", y='cnt_daily', ax=ax)
ax.set(title='INTENSITAS JUMLAH SEWA SEPEDA PERBULAN')
plt.xlabel("Month")
plt.ylabel("Jumlah Sepeda")
plt.show()


# ### 4. Bagaimana dampak cuaca(weathersit) terhadap jumlah sewa sepeda harian?

# In[35]:


plt.figure(figsize=(10, 5))
sns.boxplot(x="weathersit_daily", y="cnt_daily", data=days_hours_df)
plt.title("DAMPAK CUACA PADA JUMLAH SEWA SEPEDA HARIAN")
plt.xlabel("Weathersit")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.show()


# ### 5. Bagaimana perbedaan jumlah sepeda harian antara hari kerja(workingday) dan hari libur(holiday)?

# In[36]:


plt.figure(figsize=(10, 5))
sns.boxplot(x="workingday_daily", y="cnt_daily", data=days_hours_df)
plt.title("PERBEDAAN JUMLAH SEWA SEPEDA HARIAN ANTARA WORKINGDAY DAN HOLIDAY")
plt.xlabel("Workingday")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.show()


# ## CONCLUSION

# ### 1. Bagaimana intensitas jumlah sewa sepeda harian setiap musim(season)?

# Berdasarkan diagram bar diatas, rata-rata intensitas jumlah sewa sepeda harian paling tinggi dilakukan pada musim gugur (Fall) dan yang paling rendah dilakukan pada musim semi (Springer)

# ### 2. Bagaimana intensitas jumlah sewa sepeda harian setiap tahun(year)?

# Berdasarkan diagram bar diatas, rata-rata intensitas jumlah sewa sepeda harian paling tinggi dilakukan pada tahun 2012

# ### 3. Bagaimana intensitas jumlah sewa sepeda harian setiap bulan(month)?

# Berdasarkan diagram bar diatas, kondisi jumlah sewa sepeda pada bulan ke-6 dan ke-9 lebih banyak dibandingkan dengan bulan yang lainnya 

# ### 4. Bagaimana dampak cuaca(weathersit) terhadap jumlah sewa sepeda harian?

# Berdasarkan diagram box plot diatas, jumlah sewa sepeda harian meningkat pada cuaca Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian

# ### 5. Bagaimana perbedaan jumlah sepeda harian antara hari kerja(workingday) dan hari libur(holiday)?

# Berdasarkan diagram box plot diatas, jumlah sewa sepeda harian lebih banyak dilakukan pada workingday daripada holiday
