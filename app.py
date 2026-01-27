import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Panel de anuncios de vehículos 🚗")

car_data = pd.read_csv("vehicles_us.csv")

min_year = int(car_data["model_year"].min())
max_year = int(car_data["model_year"].max())

year_range = st.slider(
    "Selecciona rango de año del modelo",
    min_year,
    max_year,
    (min_year, max_year)
)

filtered_data = car_data[
    (car_data["model_year"] >= year_range[0]) &
    (car_data["model_year"] <= year_range[1])
]

vehicle_types = sorted(filtered_data["type"].dropna().unique())

selected_type = st.selectbox(
    "Selecciona tipo de vehículo",
    ["Todos"] + list(vehicle_types)
)

if selected_type != "Todos":
    filtered_data = filtered_data[filtered_data["type"] == selected_type]

st.write("Vista rápida del dataset:")
st.dataframe(car_data.sample(20))

show_hist = st.checkbox("Construir histograma (odómetro) 🛣️")

if show_hist:
    st.write("Creación de un histograma para la columna odómetro")
    fig = px.histogram(filtered_data, x="odometer",  title="Odómetro")
    st.plotly_chart(fig, use_container_width=True)

show_scatter = st.checkbox(
    "Construir diagrama de dispersión (precio vs odómetro) 📊")

if show_scatter:
    st.write("Creación de un diagrama de dispersión para precio vs odómetro")
    fig = px.scatter(filtered_data, x="odometer", y="price", color="fuel",
                     title="Precio vs Odómetro por Tipo de Combustible")
    st.plotly_chart(fig, use_container_width=True)
