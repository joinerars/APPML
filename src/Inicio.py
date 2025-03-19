import streamlit as st
from PIL import Image
import base64
import io  # Importamos el módulo io

def main():

    st.markdown(
        """
        <style>
            body {
                background-color: #F4F5F9;
            }
            .stApp {
                background-color: #F4F5F9; 
            }
            h1, h2, h3, h4, h5, h6, p, label {
            color: black; /* Asegura que todos los textos sean negros */
            }
        </style>
        """,
        
        unsafe_allow_html=True
    )
    
    # Cargar logo
    logo_path = "imga.png"
    logo = Image.open(logo_path)
    
        # Redimensionar el logo a la mitad de su tamaño original
    new_size = (logo.width // 4, logo.height // 4)
    logo = logo.resize(new_size)

    # Convertir la imagen a base64 para incrustarla en HTML
    buffered = io.BytesIO()
    logo.save(buffered, format="PNG")
    logo_base64 = base64.b64encode(buffered.getvalue()).decode()

    # Mostrar logo centrado con bordes redondeados
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
            <img src="data:image/png;base64,{logo_base64}" style="max-width: 50%; height: auto; margin-bottom: 20px; border-radius: 20px;">
        </div>
        """, unsafe_allow_html=True
    )

    # Mostrar título y descripción centrados
    st.markdown("""
        <h1 style='text-align: center;color: black;'>Bienvenido al Evaluador de Riesgo de Accidente Cerebrovascular</h1>
        <h3 style='text-align: center;color: black; font-size: 20px;'>Esta herramienta ayuda a evaluar el riesgo de accidente cerebrovascular basado en diversos factores de salud.</h3>
    """, unsafe_allow_html=True)

  # Botón estilizado con shadow y negrita
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #A2E4B8;
            color: black;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 30px;
            border: none;
            display: block;
            margin: 20px auto;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        }
        .stButton>button:hover {
            background-color: #8DCFA0;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.3);
        }
        </style>
    """, unsafe_allow_html=True)
    

    # Agregar botón de navegación
    if st.button("Hacer Evaluación"):
        st.session_state['page'] = 'Stroke'

    # Mostrar la siguiente interfaz si se ha activado
    if 'page' in st.session_state and st.session_state['page'] == 'Stroke':
        st.switch_page("pages/Stroke.py")




if __name__ == "__main__":
    main()