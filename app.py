# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Neo-Bank Engagement", layout="wide")

# Cargar datos
df = pd.read_csv("data/df.csv")  # Ajusta la ruta si usas otro archivo

# Agrupar usuarios únicos por país
country_users = (
    df.groupby('country')['user_id']
    .nunique()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
    .rename(columns={'user_id': 'unique_users'})
)

# Título
st.title("Neo-Bank")

# Gráfico
fig = px.bar(
    country_users,
    x="country", 
    y="unique_users",
    title="Top países por usuarios únicos"
)
st.plotly_chart(fig, use_container_width=True)
