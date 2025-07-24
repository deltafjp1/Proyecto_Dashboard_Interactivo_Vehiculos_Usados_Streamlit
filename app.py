import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('vehicles_us.csv')
car_data = df.copy()

# Título
st.title('Cantidad de Vehículos Usados en Estados Unidos')

# Encabezado
st.header(
    'Visualización de la Cantidad de Kilómetros Recorridos por Vehículos Usados')

# Botón para construir los gráficos
hist_button = st.button('Construir gráfico')

# Variable para controlar la reconstrucción con el checkbox
build_histogram = False

if hist_button:
    st.write('Creación de un histograma y gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Histograma
    hist_fig = px.histogram(car_data, x="odometer")
    st.subheader('Histograma del Odómetro')
    st.plotly_chart(hist_fig, use_container_width=True)

    # Gráfico de dispersión
    scatter_fig = px.scatter(
        car_data, x="odometer", y="price", title="Relación entre Kilometraje y Precio")
    st.subheader('Gráfico de Dispersión (Odometer vs Precio)')
    st.plotly_chart(scatter_fig, use_container_width=True)

    # Mostrar el checkbox
    build_histogram = st.checkbox(
        '¿Deseas volver a construir otro histograma?')

# Si el checkbox está marcado
if build_histogram:
    st.write('Reconstrucción del histograma para la columna "odometer"')
    fig2 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig2, use_container_width=True)
