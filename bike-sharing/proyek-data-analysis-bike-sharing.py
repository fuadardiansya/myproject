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

#Cleaning Data
#Membersihkan tabel days_df
days_df.duplicated().sum()
#Membersihkan tabel hours_df
hours_df.duplicated().sum()
#Membersihkan tabel days_hours_df
days_hours_df.duplicated().sum()

#Menghapus duplikat tabel days_df
days_df.drop_duplicates(inplace=True)
#Menghapus duplikat tabel hours_df
hours_df.drop_duplicates(inplace=True)
#Menghapus duplikat tabel days_hours_df
days_hours_df.drop_duplicates(inplace=True)

print("Jumlah duplikasi: ", days_df.duplicated().sum())
print("Jumlah duplikasi: ", hours_df.duplicated().sum())
print("Jumlah duplikasi: ", days_hours_df.duplicated().sum())

#Missing values tabel days_df
days_df.isna().sum()
#Missing values tabel hours_df
hours_df.isna().sum()
#Missing values tabel days_hours_df
days_hours_df.isna().sum()

#inaccurate tabel days_df
days_df.describe()
#inaccurate tabel hours_df
hours_df.describe()
#inaccurate tabel days_hours_df
days_hours_df.describe()

#Exploratory Data Analysis
days_df.sample(5)
days_df.describe(include="all")
hours_df.sample(5)
hours_df.describe(include="all")
days_hours_df.sample(5)
days_hours_df.describe(include="all")

days_hours_df.instant_daily.is_unique
days_hours_df.instant_daily.duplicated

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
#1.Bagaimana intensitas jumlah sewa sepeda harian setiap musim(season)?
#Seaborn_bar
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="season_daily", y='cnt_daily', ax=ax)
ax.set(title='INTENSITAS JUMLAH SEWA SEPEDA HARIAN SETIAP MUSIM')
plt.xlabel("Season")
plt.ylabel("Rata-Rata Jumlah Sewa Sepeda Harian")
plt.show()

#2.Bagaimana intensitas jumlah sewa sepeda harian setiap tahun(year)?
#Seaborn_bar
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="yr_daily", y='cnt_daily', ax=ax)
ax.set(title='INTENSITAS JUMLAH SEWA SEPEDA PERTAHUN')
plt.xlabel("Year")
plt.ylabel("Jumlah Sepeda")
plt.show()

#3.Bagaimana intensitas jumlah sewa sepeda harian setiap bulan(month)?
#Seaborn_bar
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="mnth_daily", y='cnt_daily', ax=ax)
ax.set(title='INTENSITAS JUMLAH SEWA SEPEDA PERBULAN')
plt.xlabel("Month")
plt.ylabel("Jumlah Sepeda")
plt.show()

#4.Bagaimana dampak cuaca(weathersit) terhadap jumlah sewa sepeda harian?
#Seaborn_bar
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="weathersit_daily", y='cnt_daily', ax=ax)
ax.set(title='DAMPAK CUACA PADA JUMLAH SEWA SEPEDA HARIAN')
plt.xlabel("Weathersit")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.show()

#5.Bagaimana perbedaan jumlah sepeda harian antara hari kerja(workingday) dan hari libur(holiday)?
#Seaborn_boxplot
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=days_hours_df, x="workingday_daily", y='cnt_daily', ax=ax)
ax.set(title='PERBEDAAN JUMLAH SEWA SEPEDA HARIAN ANTARA WORKINGDAY DAN HOLIDAY')
plt.xlabel("Workingday")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.show()

st.pyplot(fig)

st.caption('Copyright © Fuad Hidayat Ardiansya 2023')






















