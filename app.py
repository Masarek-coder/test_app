import streamlit as st
import pandas as pd
import scipy

st.title("¡Mi Aplicación en Python!")

st.write("Si puedes leer esto, Streamlit está funcionando.")

# Creamos unos datos de prueba con Pandas
df = pd.DataFrame({
    'Columna A': [1, 2, 3, 4],
    'Columna B': [10, 20, 30, 40]
})

st.write("Aquí mostramos un DataFrame de Pandas:", df)
st.write(f"Versión de Scipy detectada: {scipy.__version__}")