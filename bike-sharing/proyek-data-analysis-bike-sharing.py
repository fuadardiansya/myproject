#Menyiapkan library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#Membaca dataset
days_df = pd.read_csv("https://raw.githubusercontent.com/fuadardiansya/myproject/main/bike-sharing/day.csv")
#Menampilkan dataset
days_df.head()

#Membaca dataset
hours_df = pd.read_csv("https://raw.githubusercontent.com/fuadardiansya/myproject/main/bike-sharing/hour.csv")
#Menampilkan dataset
hours_df.head()

#Menghitung jumlah dataframe
print("Jumlah dataframe day:", days_df.shape[0])
print("Jumlah dataframe hour:", hours_df.shape[0])

#Mengabungkan dataframe
days_hours_df = days_df.merge(hours_df, on='dteday', how='inner', suffixes=('_daily','_hourly'))
print(days_hours_df.shape)

#Menampilkan hasil penggabungan dataframe
#days_hours_df.loc[days_hours_df["dteday"].isnull()]
#days_hours_df.head()

#Memeriksa dataframe days_df
days_df.info()
#Memeriksa dataframe hours_df
hours_df.info()
#Memeriksa dataframe days_hours_df
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

#Mendefinisikan fungsi yang akan digunakan
def range(series):
   return series.max() - series.min()
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

#Bar Chart
st.header('Dashboard Proyek Data Analysis Bike Sharing')
st.subheader('Check this out')

data_musimku = days_hours_df.groupby("season_daily")["cnt_daily"].mean()
jenis_musim = ["Springer","Summer","Fall", "Winter"]
plt.figure(figsize=(10, 5))
plt.bar(jenis_musim, data_musimku)
plt.title("INTENSITAS JUMLAH SEWA SEPEDA HARIAN SETIAP MUSIM")
plt.xlabel("Season")
plt.ylabel("Rata-Rata Jumlah Sewa Sepeda Harian")
plt.show()

#Bar Chart
data_tahunku = days_hours_df.groupby("yr_daily")["cnt_daily"].mean()
jenis_tahun = ["2011","2012"]
plt.figure(figsize=(10, 5))
plt.bar(jenis_tahun, data_tahunku)
plt.title("INTENSITAS JUMLAH SEWA SEPEDA HARIAN SETIAP TAHUN")
plt.xlabel("Season")
plt.ylabel("Rata-Rata Jumlah Sewa Sepeda Harian")
plt.show()

#Bar Plot
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="mnth_daily", y='cnt_daily', ax=ax)
ax.set(title='INTENSITAS JUMLAH SEWA SEPEDA PERBULAN')
plt.xlabel("Month")
plt.ylabel("Jumlah Sepeda")
plt.show()

#Boxplot
plt.figure(figsize=(10, 5))
sns.boxplot(x="weathersit_daily", y="cnt_daily", data=days_hours_df)
plt.title("DAMPAK CUACA PADA JUMLAH SEWA SEPEDA HARIAN")
plt.xlabel("Weathersit")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.show()

#Boxplot

plt.figure(figsize=(10, 5))
sns.boxplot(x="workingday_daily", y="cnt_daily", data=days_hours_df)
plt.title("PERBEDAAN JUMLAH SEWA SEPEDA HARIAN ANTARA WORKINGDAY DAN HOLIDAY")
plt.xlabel("Workingday")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.show()

st.pyplot(fig)
st.caption('Copyright © Fuad Hidayat Ardiansya 2023')
