import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuración
st.set_page_config(page_title="Registro AIR-E", layout="wide")
st.title("📝 Cambios de Dirección")

# Archivo CSV temporal (se crea automáticamente)
CSV_PATH = "datos_cambios.csv"

# Cargar o crear CSV
if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
else:
    df = pd.DataFrame(columns=["Asunto", "NIC", "Dirección", "Fecha"])

# Formulario
with st.form("Formulario"):
    asunto = st.text_input("Asunto*")
    nic = st.text_input("NIC*")
    direccion = st.text_area("Dirección*")
    submitted = st.form_submit_button("Guardar")
    
    if submitted:
        nuevo_registro = pd.DataFrame({  # Corregido: Llaves cerradas correctamente
            "Asunto": [asunto],
            "NIC": [nic],
            "Dirección": [direccion],
            "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        })  # ¡Esta llave cierra el diccionario!
        
        df = pd.concat([df, nuevo_registro], ignore_index=True)
        df.to_csv(CSV_PATH, index=False)
        st.success("¡Guardado! Usa Power Automate para pasarlo a OneDrive.")

# Mostrar datos
st.dataframe(df)

# Botón para abrir el CSV (opcional)
if st.button("📂 Abrir carpeta del archivo"):
    os.startfile(os.path.dirname(os.path.abspath(CSV_PATH