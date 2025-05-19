import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("segmentasi_pelanggan_final.csv")

st.set_page_config(page_title="Dashboard Segmentasi Pelanggan", layout="wide")
st.title("Dashboard Segmentasi Pelanggan Pembiayaan Mobil")

# Filter segmen
segmen_filter = st.multiselect(
    "Filter Segmen Pelanggan",
    options=data['segmen'].unique(),
    default=data['segmen'].unique()
)

data_filtered = data[data['segmen'].isin(segmen_filter)]

# Ringkasan jumlah pelanggan per segmen
st.subheader("Distribusi Pelanggan per Segmen")
segmen_counts = data_filtered['segmen'].value_counts()
st.dataframe(segmen_counts.rename("Jumlah Pelanggan"))

# Pie Chart
fig1, ax1 = plt.subplots()
ax1.pie(segmen_counts, labels=segmen_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Bar plot: rata-rata pendapatan per segmen
st.subheader("Rata-rata Pendapatan Bulanan per Segmen")
avg_income = data_filtered.groupby('segmen')['pendapatan_bulanan'].mean().sort_values()
fig2, ax2 = plt.subplots()
sns.barplot(x=avg_income.values, y=avg_income.index, ax=ax2)
ax2.set_xlabel("Pendapatan Bulanan (Rp)")
st.pyplot(fig2)

# Tabel data pelanggan
st.subheader("Data Pelanggan")
st.dataframe(data_filtered)

# Unduh hasil segmentasi
st.download_button(
    "Unduh Data Segmentasi (csv)",
    data=data_filtered.to_csv(index=False).encode('utf-8'),
    file_name="segmentasi_terfilter.csv",
    mime='text/csv
)