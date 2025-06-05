import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(page_title="Sistema de Cambios de Dirección AIR-E", layout="wide")
st.title("📝 Registro de Cambios de Dirección")

# Archivos
CSV_TEMP = "datos_temp.csv"  # Archivo temporal (se crea automáticamente)
EXCEL_ONEDRIVE = r"C:\Users\jean.dominguez\OneDrive - Air-e SAS ESP\cambios de dir 2025\CAMBIOS DE DIRECCION 2025.xlsx"

# Cargar o crear datos temporales
if os.path.exists(CSV_TEMP):
    df_temp = pd.read_csv(CSV_TEMP)
else:
    df_temp = pd.DataFrame(columns=["Asunto", "NIC", "Dirección", "Timestamp"])

# Formulario Streamlit
with st.form("Formulario"):
    asunto = st.text_input("Asunto*")
    nic = st.text_input("NIC*")
    direccion = st.text_area("Dirección*")
    submitted = st.form_submit_button("Guardar")

    if submitted:
        nuevo_registro = {
            "Asunto": asunto,
            "NIC": nic,
            "Dirección": direccion,
           
