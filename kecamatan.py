import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)
df = pd.read_excel('KecamatanAgustus2023.xlsx')

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
st.title("Kecamatan Terbaik Berdasarkan Kota/Povinsi")

# Create dropdown list with 'All' option
city_options = ['All'] + list(df["Kota"].unique())
selected_city = st.selectbox("Choose a city", city_options)

# Display data based on selected city
if selected_city == 'All':
    selected_rows = df  # Show all rows
else:
    selected_rows = df[df["Kota"] == selected_city]  # Filter by selected city

# Create count plot
plt.figure(figsize=(20, 10))
ax = sns.countplot(data=selected_rows, x=' kecamatan', order=selected_rows[' kecamatan'].value_counts().head(10).index)
plt.xticks(rotation=20, size=20)
plt.title(f"Count Plot for Kecamatan in {selected_city if selected_city != 'All' else 'All Cities'}")
plt.tight_layout()

# Annotate the bars with count values
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=12, color='gray', xytext=(0, 5),
                textcoords='offset points')

# Display the plot using st.pyplot
st.pyplot()

selected_region = st.selectbox("Choose a region", df["Provinsi"].unique())

# Display data based on selected city
selected_rows2 = df[df["Provinsi"] == selected_region]

plt.figure(figsize=(20, 10))
ax = sns.countplot(data=selected_rows2, x=' kecamatan', order=selected_rows2[' kecamatan'].value_counts().head(10).index)
plt.xticks(rotation=20, size=20)
plt.title(f"Count Plot for Kecamatan in {selected_region}")
plt.tight_layout()

# Annotate the bars with count values
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=12, color='gray', xytext=(0, 5),
                textcoords='offset points')

st.pyplot()
