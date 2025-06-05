import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(page_title="Sistema de Cambios de Dirección", layout="wide")

# Título
st.title("📝 Registro de Cambios de Dirección")

# Nombre del archivo donde se guardarán los datos
EXCEL_FILE = "cambios_de_dir.xlsx"

# Cargar datos existentes o crear nuevo DataFrame
if os.path.exists(EXCEL_FILE):
    df = pd.read_excel(EXCEL_FILE)
else:
    df = pd.DataFrame(columns=[
        "Asunto", "Reportado por", "# Radicado (Anexo)", "NIC / CUENTA",
        "Tipo de Cambio", "Fecha de Inicio", "Dirección - Barrio Anterior",
        "Dirección - Barrio Nueva", "Observaciones", "Analista",
        "DIR NUEVA EN OPS", "Fecha de Realización", "Estatus", "COMENTARIO", "NPN"
    ])

# Formulario para nuevos registros
with st.expander("➕ Agregar Nuevo Registro", expanded=True):
    with st.form("nuevo_registro", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            asunto = st.text_input("Asunto*", max_chars=100)
            reportado_por = st.text_input("Reportado por*", max_chars=50)
            radicado = st.text_input("# Radicado (Anexo)", max_chars=20)
            nic_cuenta = st.text_input("NIC / CUENTA*", max_chars=20)
            tipo_cambio = st.selectbox("Tipo de Cambio", ["Residencial", "Comercial", "Otro"])
            fecha_inicio = st.date_input("Fecha de Inicio*", datetime.now())
            dir_anterior = st.text_area("Dirección - Barrio Anterior*", max_chars=200)
            
        with col2:
            dir_nueva = st.text_area("Dirección - Barrio Nueva*", max_chars=200)
            observaciones = st.text_area("Observaciones", max_chars=300)
            analista = st.text_input("Analista", max_chars=50)
            dir_nueva_ops = st.text_input("DIR NUEVA EN OPS", max_chars=200)
            fecha_realizacion = st.date_input("Fecha de Realización")
            estatus = st.selectbox("Estatus", ["Pendiente", "En Proceso", "Completado", "Rechazado"])
            comentario = st.text_area("COMENTARIO", max_chars=200)
            npn = st.text_input("NPN", max_chars=20)
        
        submitted = st.form_submit_button("Guardar Registro")
        
        if submitted:
            if not asunto or not reportado_por or not nic_cuenta or not dir_anterior or not dir_nueva:
                st.error("Por favor complete los campos obligatorios (*)")
            else:
                new_entry = {
                    "Asunto": asunto,
                    "Reportado por": reportado_por,
                    "# Radicado (Anexo)": radicado,
                    "NIC / CUENTA": nic_cuenta,
                    "Tipo de Cambio": tipo_cambio,
                    "Fecha de Inicio": fecha_inicio,
                    "Dirección - Barrio Anterior": dir_anterior,
                    "Dirección - Barrio Nueva": dir_nueva,
                    "Observaciones": observaciones,
                    "Analista": analista,
                    "DIR NUEVA EN OPS": dir_nueva_ops,
                    "Fecha de Realización": fecha_realizacion,
                    "Estatus": estatus,
                    "COMENTARIO": comentario,
                    "NPN": npn
                }
                
                df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
                df.to_excel(EXCEL_FILE, index=False)
                st.success("¡Registro guardado exitosamente!")

# Mostrar todos los registros
st.divider()
st.subheader("📊 Registros Existentes")

# Opción para editar registros
if not df.empty:
    edited_df = st.data_editor(
        df,
        key="data_editor",
        use_container_width=True,
        num_rows="dynamic",
        column_config={
            "Fecha de Inicio": st.column_config.DateColumn(),
            "Fecha de Realización": st.column_config.DateColumn()
        }
    )
    
    if st.button("Guardar Cambios"):
        edited_df.to_excel(EXCEL_FILE, index=False)
        st.success("Cambios guardados en el archivo Excel")
        
    # Opción para descargar el Excel
    st.download_button(
        label="📥 Descargar Excel",
        data=pd.read_excel(EXCEL_FILE).to_csv(index=False).encode('utf-8'),
        file_name="cambios_de_dir.csv",
        mime="text/csv"
    )
else:
    st.info("No hay registros aún. Agrega uno usando el formulario arriba.")

# Instrucciones para desplegar
st.sidebar.markdown("""
### 🚀 Cómo usar esta aplicación
1. Completa el formulario con los datos del cambio
2. Los datos se guardan automáticamente en un archivo Excel
3. Puedes editar registros directamente en la tabla
4. Descarga los datos cuando lo necesites

### ☁️ Para desplegar en la nube:
1. Crea una cuenta en [Streamlit Cloud](https://streamlit.io/cloud)
2. Sube este script como un repositorio en GitHub
3. Conéctalo a Streamlit Cloud
""")
