import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache
def load_data():
    return pd.read_excel('KecamatanAgustus2023.xlsx')

@st.cache
def load_data2():
    return pd.read_excel('KotaAgustus2023.xlsx')

df = load_data()
df2 = load_data2()

# Set Streamlit options
st.set_option('deprecation.showPyplotGlobalUse', False)

# Set background color and title
st.markdown('<style>body{background-color: Blue;}</style>', unsafe_allow_html=True)
st.title("Kecamatan Terbaik Berdasarkan Kota/Povinsi")

# Dropdown for City selection
city_options = ['All'] + list(df["Kota"].unique())
selected_city = st.selectbox("Choose a city", city_options)

# Dropdown for Region selection
region_options = ['All'] + list(df2["Provinsi"].unique())
selected_region = st.selectbox("Choose a region", region_options)

# Filter data based on selections
if selected_city == 'All':
    selected_rows_city = df
else:
    selected_rows_city = df[df["Kota"] == selected_city]

if selected_region == 'All':
    selected_rows_region = df2  # Show all rows
else:
    selected_rows_region = df2[df2["Provinsi"] == selected_region]

# Function to create and display count plot
def display_count_plot(data, x_column, title):
    plt.figure(figsize=(20, 10))
    ax = sns.countplot(data=data, x=x_column, order=data[x_column].value_counts().head(10).index)
    plt.xticks(rotation=20, size=20)
    plt.title(title)
    plt.tight_layout()

    # Annotate the bars with count values
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=12, color='gray', xytext=(0, 5),
                    textcoords='offset points')

    st.pyplot()

# Display count plots
display_count_plot(selected_rows_city, ' kecamatan', f"Count Plot for Kecamatan in {selected_city if selected_city != 'All' else 'All Cities'}")
display_count_plot(selected_rows_region, 'Kota', f"Count Plot for Kota in {selected_region}")
