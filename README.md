# Used Vehicles EDA App | Streamlit Data Analysis Project

🇪🇸 Aplicación interactiva en Streamlit para explorar patrones de precio, kilometraje y distribución de vehículos usados.
🇬🇧 Interactive Streamlit app to explore price, mileage, and distribution patterns in used vehicle listings.

---


[Ver app / View app](https://proyecto-sprint-7-2p3r.onrender.com/)  
[Ver repositorio / View repository](https://github.com/deltafjp1/Proyecto_Dashboard_Interactivo_Vehiculos_Usados_Streamlit)
---

## Descripción / Overview

🇪🇸
Este proyecto presenta una aplicación web desarrollada con Streamlit para realizar un análisis exploratorio de datos sobre anuncios de vehículos usados. La app permite visualizar la distribución del kilometraje y explorar la relación entre kilometraje y precio mediante gráficos interactivos.

El objetivo es facilitar una exploración rápida del dataset y ayudar a identificar patrones generales, posibles valores atípicos y relaciones útiles para entender el comportamiento del mercado de vehículos usados.

🇬🇧
This project presents a Streamlit web application for exploratory data analysis of used vehicle listings. The app allows users to visualize mileage distribution and explore the relationship between mileage and price through interactive charts.

The goal is to support quick dataset exploration and help identify general patterns, possible outliers, and useful relationships to understand used vehicle market behavior.

---

## Objetivo / Objective

🇪🇸
Construir una aplicación interactiva que permita analizar visualmente el comportamiento del kilometraje y su relación con el precio en anuncios de vehículos usados.

🇬🇧
Build an interactive application to visually analyze mileage behavior and its relationship with price in used vehicle listings.

---

## Preguntas de negocio / Business Questions

🇪🇸

* ¿Cómo se distribuye el kilometraje de los vehículos usados?
* ¿Existe una relación visible entre kilometraje y precio?
* ¿Qué vehículos podrían considerarse valores atípicos por precio o kilometraje?
* ¿Cómo puede una visualización interactiva facilitar el análisis exploratorio del mercado automotor?

🇬🇧

* How is mileage distributed across used vehicles?
* Is there a visible relationship between mileage and price?
* Which vehicles could be considered outliers based on price or mileage?
* How can an interactive visualization support exploratory analysis of the automotive market?

---

## Datos / Data

🇪🇸
El análisis utiliza el archivo `vehicles_us.csv`, un dataset de anuncios de vehículos usados en Estados Unidos. Incluye variables relacionadas con precio, kilometraje, características del vehículo y datos del anuncio.

🇬🇧
The analysis uses the `vehicles_us.csv` file, a dataset of used vehicle listings in the United States. It includes variables related to price, mileage, vehicle characteristics, and listing information.

---

## Proceso / Process

🇪🇸

1. Carga del dataset `vehicles_us.csv`.
2. Preparación inicial de los datos con pandas.
3. Construcción de una aplicación web con Streamlit.
4. Creación de un histograma para analizar la distribución del kilometraje.
5. Creación de un gráfico de dispersión para analizar la relación entre kilometraje y precio.
6. Publicación de la aplicación para consulta interactiva.

🇬🇧

1. Loading the `vehicles_us.csv` dataset.
2. Initial data preparation with pandas.
3. Development of a web application with Streamlit.
4. Creation of a histogram to analyze mileage distribution.
5. Creation of a scatter plot to analyze the relationship between mileage and price.
6. Deployment of the application for interactive use.

---

## Funcionalidades / Features

* Histograma interactivo de kilometraje / Interactive mileage histogram.
* Gráfico de dispersión precio vs. kilometraje / Price vs. mileage scatter plot.
* Exploración rápida tipo self-service / Quick self-service exploration.
* Visualizaciones interactivas con Plotly Express / Interactive visualizations with Plotly Express.

---

## Herramientas / Tools

* Python
* Streamlit
* pandas
* Plotly Express
* Render

---

## Insights clave / Key Insights

🇪🇸

* El histograma permite identificar la concentración de vehículos según su kilometraje.
* El gráfico de dispersión ayuda a explorar si los vehículos con mayor kilometraje tienden a mostrar precios más bajos.
* La visualización interactiva facilita la detección de posibles valores atípicos.
* La app permite que usuarios no técnicos exploren el dataset sin ejecutar código.

🇬🇧

* The histogram helps identify the concentration of vehicles by mileage.
* The scatter plot helps explore whether vehicles with higher mileage tend to show lower prices.
* Interactive visualization supports the detection of possible outliers.
* The app allows non-technical users to explore the dataset without running code.

---

## Recomendación / Recommendation

🇪🇸
En un contexto laboral real, esta aplicación podría evolucionar hacia una herramienta de análisis de mercado automotor, incorporando filtros por marca, modelo, año, condición, tipo de combustible o rango de precio para apoyar decisiones de compra, venta o pricing.

🇬🇧
In a real business context, this application could evolve into an automotive market analysis tool by adding filters for brand, model, year, condition, fuel type, or price range to support buying, selling, or pricing decisions.

---

## Estructura del repositorio / Repository Structure

```text
Proyecto_Dashboard_Interactivo_Vehiculos_Usados_Streamlit/
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── README.md
```

---

## Cómo ejecutar localmente / How to Run Locally

### 1. Clonar el repositorio / Clone the repository

```bash
git clone https://github.com/deltafjp1/Proyecto_Dashboard_Interactivo_Vehiculos_Usados_Streamlit.git
```

### 2. Entrar a la carpeta del proyecto / Enter the project folder

```bash
cd Proyecto_Dashboard_Interactivo_Vehiculos_Usados_Streamlit
```

### 3. Instalar dependencias / Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación / Run the app

```bash
streamlit run app.py
```

---

## Notas / Notes

🇪🇸

* El proyecto está enfocado en análisis exploratorio de datos y visualización interactiva.
* La app fue desarrollada como una herramienta simple para explorar patrones básicos del dataset.
* Este caso demuestra habilidades de despliegue de aplicaciones de datos usando Streamlit.

🇬🇧

* The project focuses on exploratory data analysis and interactive visualization.
* The app was developed as a simple tool to explore basic dataset patterns.
* This case demonstrates skills in deploying data applications using Streamlit.

