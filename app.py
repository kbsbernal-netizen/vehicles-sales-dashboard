import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.header('Analisis de anuncios de venta de vehiculos en EE. UU.')

st.write(
    'Explora el conjunto de datos de anuncios de venta de coches usando los botones '
    'de abajo para generar cada visualizacion.'
)

st.dataframe(car_data.head(20))

# Boton para construir un histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Histograma de la distribucion del odometro (kilometraje)')
    fig = px.histogram(car_data, x='odometer', nbins=60)
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificacion para construir un grafico de dispersion
scatter_checkbox = st.checkbox('Construir grafico de dispersion (precio vs. odometro)')
if scatter_checkbox:
    st.write('Grafico de dispersion: precio vs. kilometraje (odometer)')
    fig = px.scatter(car_data, x='odometer', y='price', opacity=0.4)
    st.plotly_chart(fig, use_container_width=True)
