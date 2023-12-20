#Menyiapkan Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#Gathering Data
#Membaca dataset day.csv
days_df = pd.read_csv("https://raw.githubusercontent.com/fuadardiansya/myproject/main/bike-sharing/day.csv")
#Menampilkan dataset
days_df.head()

#Membaca dataset hour.csv
hours_df = pd.read_csv("https://raw.githubusercontent.com/fuadardiansya/myproject/main/bike-sharing/hour.csv")
#Menampilkan dataset
hours_df.head()

#Menghitung jumlah dataframe
print("Jumlah dataframe day:", days_df.shape[0])
print("Jumlah dataframe hour:", hours_df.shape[0])

#Assessing Data
#Mengabungkan dataframe
days_hours_df = days_df.merge(hours_df, on='dteday', how='inner', suffixes=('_daily','_hourly'))
print(days_hours_df.shape)
#Menampilkan hasil penggabungan dataframe
#days_hours_df.loc[days_hours_df["dteday"].isnull()]
#days_hours_df.head()

#Menilai tabel days_df
days_df.info()
#Menilai tabel hours_df
hours_df.info()
#Menilai tabel days_hours_df
days_hours_df.info()

#Memeriksa jumlah missing values days_df
days_df.isna().sum()
#Memeriksa jumlah missing values hours_df
hours_df.isna().sum()
#Memeriksa jumlah missing values days_hours_df
days_hours_df.isna().sum()

print("Jumlah duplikat: ", days_df.duplicated().sum())
print("Jumlah duplikat: ", hours_df.duplicated().sum())
print("Jumlah duplikat: ", days_hours_df.duplicated().sum())

#Menampilkan ringkasan dataframe days_df
days_df.describe()
#Menampilkan ringkasan dataframe hours_df
hours_df.describe()
#Menampilkan ringkasan dataframe days_hours_df
days_hours_df.describe()

#Exploratory Data Analysis
days_df.sample(5)
days_df.describe(include="all")
hours_df.sample(5)
hours_df.describe(include="all")
days_hours_df.sample(5)
days_hours_df.describe(include="all")

days_hours_df.groupby(by="season_hourly").agg({
    "workingday_hourly": "count", #Menjumlahkan penyewa pada hari kerja berdasarkan musim
    "windspeed_hourly": ["max", "min", "mean", lambda x: x.max() - x.min()] #Membuat fungsi kustom untuk range
}).sort_values(by=("workingday_hourly", "count"), ascending=False)

days_hours_df.groupby(by="season_daily").agg({
    "workingday_hourly": "count", #Menjumlahkan penyewa pada hari kerja berdasarkan musim
    "windspeed_hourly": ["max", "min", "mean", lambda x: x.max() - x.min()] #Membuat fungsi kustom untuk range
}).sort_values(by=("workingday_hourly", "count"), ascending=False)

days_hours_df.groupby(by="season_daily").mnth_daily.nunique().sort_values(ascending=False)
days_hours_df.groupby(by="season_daily").instant_daily.nunique().sort_values(ascending=False)
days_hours_df.groupby(by="season_daily").cnt_daily.nunique().sort_values(ascending=False)
days_hours_df.groupby(by="season_daily").cnt_hourly.nunique().sort_values(ascending=False)
days_hours_df.groupby(by="weathersit_daily").cnt_daily.nunique().sort_values(ascending=False)
days_hours_df.groupby(by="weathersit_daily").cnt_hourly.nunique().sort_values(ascending=False)
days_hours_df.groupby(by="mnth_daily").cnt_daily.nunique().sort_values(ascending=False)
days_hours_df.groupby(by="mnth_daily").cnt_hourly.nunique().sort_values(ascending=False)

#Mencari Value Korelasi Setiap Data perhari
numerical_columns = ["holiday_daily","weekday_daily","workingday_daily","weathersit_daily","temp_daily","atemp_daily","season_daily", "windspeed_daily",  "cnt_daily"]
correlation = days_hours_df[numerical_columns].corr()
print(correlation)

#Visualization & Explanatory Analysis
st.header('Dashboard Proyek Data Analysis - Bike Sharing')

#1.Bagaimana intensitas jumlah sewa sepeda harian setiap musim(season)?
st.subheader('Bagaimana intensitas jumlah sewa sepeda harian setiap musim(season)?')

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="season_daily", y='cnt_daily', ax=ax)
ax.set(title='INTENSITAS JUMLAH SEWA SEPEDA HARIAN SETIAP MUSIM')
plt.xlabel("Season")
plt.ylabel("Rata-Rata Jumlah Sewa Sepeda Harian")
plt.show()
st.pyplot(fig)

st.markdown('''
    :red[1 adalah Springer] :orange[2 adalah Summer] :green[3 adalah Fall] :blue[4 adalah Winter].''')
kal1 = ''' Berdasarkan diagram bar diatas, rata-rata intensitas jumlah sewa sepeda harian paling tinggi 
dilakukan pada musim gugur (Fall) dan yang paling rendah dilakukan pada musim semi (Springer)
'''
st.markdown(kal1)

#2.Bagaimana intensitas jumlah sewa sepeda harian setiap tahun(year)?
st.subheader('Bagaimana intensitas jumlah sewa sepeda harian setiap tahun(year)?')

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="yr_daily", y='cnt_daily', ax=ax)
ax.set(title='INTENSITAS JUMLAH SEWA SEPEDA PERTAHUN')
plt.xlabel("Year")
plt.ylabel("Jumlah Sepeda")
plt.show()
st.pyplot(fig)

st.markdown('''
    :red[0 adalah 2011] :orange[1 adalah 2012].''')
kal2 = '''Berdasarkan diagram bar diatas, rata-rata intensitas jumlah sewa sepeda harian 
paling tinggi dilakukan pada tahun 2012
'''
st.markdown(kal2)

#3.Bagaimana intensitas jumlah sewa sepeda harian setiap bulan(month)?
st.subheader('Bagaimana intensitas jumlah sewa sepeda harian setiap bulan(month)?')

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="mnth_daily", y='cnt_daily', ax=ax)
ax.set(title='INTENSITAS JUMLAH SEWA SEPEDA PERBULAN')
plt.xlabel("Month")
plt.ylabel("Jumlah Sepeda")
plt.show()
st.pyplot(fig)

#4.Bagaimana dampak cuaca(weathersit) terhadap jumlah sewa sepeda harian?
st.subheader('Bagaimana dampak cuaca(weathersit) terhadap jumlah sewa sepeda harian?')

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="weathersit_daily", y='cnt_daily', ax=ax)
ax.set(title='DAMPAK CUACA PADA JUMLAH SEWA SEPEDA HARIAN')
plt.xlabel("Weathersit")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.show()
st.pyplot(fig)

#5.Bagaimana perbedaan jumlah sepeda harian antara hari kerja(workingday) dan hari libur(holiday)?
st.subheader('Bagaimana perbedaan jumlah sepeda harian antara hari kerja(workingday) dan hari libur(holiday)?')

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="workingday_daily", y='cnt_daily', ax=ax)
ax.set(title='PERBEDAAN JUMLAH SEWA SEPEDA HARIAN ANTARA WORKINGDAY DAN HOLIDAY')
plt.xlabel("Workingday")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.show()
st.pyplot(fig)

st.caption('Copyright © Fuad Hidayat Ardiansya 2023')






















