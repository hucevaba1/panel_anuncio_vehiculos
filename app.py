import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Panel de anuncios de vehículos 🚗")

car_data = pd.read_csv("vehicles_us.csv")

st.write("Vista rápida del dataset:")
st.dataframe(car_data.head(20))

hist_button = st.button("Construir histograma (odómetro) 🛣️")

if hist_button:
    st.write("Creación de un histograma para la columna odómetro")
    fig = px.histogram(car_data, x="odometer",  title="Odómetro")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button(
    "Construir diagrama de dispersión (precio vs odómetro) 📊")

if scatter_button:
    st.write("Creación de un diagrama de dispersión para precio vs odómetro")
    fig = px.scatter(car_data, x="odometer", y="price", color="fuel",
                     title="Precio vs Odómetro por Tipo de Combustible")
    st.plotly_chart(fig, use_container_width=True)
