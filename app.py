import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv("vehicles_us.csv")
hist_button = st.button('Construir histograma') # crear un botón
disp_button = st.button('Construir grafico de dispersion') # crear un botón

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig_hist = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig_hist, use_container_width=True)
            
if disp_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un grafico de dispersion')
            
            # crear un histograma
            fig_disp = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig_disp, use_container_width=True)

