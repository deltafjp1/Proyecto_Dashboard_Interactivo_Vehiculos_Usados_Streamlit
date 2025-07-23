import streamlit as st
import pandas as pd
import plotly_express as px


df = pd.read_csv('vehicles_us.csv')
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos


build_histogram = False

st.title('Cantidad de Vehículos Usados en Estados Unidos')

st.header(
    'Visualización de la Cantidad de kilometros Recorridos por Vehículos Usados')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Mostrar histograma
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

    build_histogram = st.checkbox(
        '¿Deseas volver a construir otro histograma?')


if build_histogram:
    st.write('Construcción adicional del histograma para columna odómetro')
    fig2 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig2, use_container_width=True)
