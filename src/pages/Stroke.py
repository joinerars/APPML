import streamlit as st
import pandas as pd

def main():
    st.markdown(
    """
    <style>
        body {
            background-color: #F4FAF0;  /* Azul claro */
        }
        .stApp {
            background-color: #F4FAF0;  /* Azul claro */
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: black; /* Asegura que todos los textos sean negros */
        }
        /* Estilo para el ícono del tooltip (signo de interrogación) */
        .stTooltipIcon svg {
            fill: gray !important; /* Cambia el color del ícono a gris */
        }
        /* Estilo para el contenido del tooltip */
        .stTooltipContent {
            background-color: white !important; /* Fondo blanco */
            color: gray !important; /* Letra gris */
            border: 1px solid #ccc !important; /* Borde gris claro */
            border-radius: 5px !important; /* Bordes redondeados */
            padding: 10px !important; /* Espaciado interno */
        }
        /* Estilo para el campo de edad */
        .stNumberInput input {
            background-color: white !important; /* Fondo blanco */
            color: black !important; /* Letra negra */
        }
        /* Estilo para los botones de incremento y decremento en el campo de edad */
        .stNumberInput button {
            background-color: #A2E4B8 !important; /* Fondo verde */
            color: white !important; /* Letra blanca */
            border: 1px solid #A2E4B8 !important; /* Borde verde */
        }
        .stNumberInput button:hover {
            background-color: #64AC8F !important; /* Fondo verde oscuro al pasar el cursor */
            border-color: #64AC8F !important; /* Borde verde oscuro al pasar el cursor */
        }
        /* Estilo para los checkboxes */
        .stCheckbox label {
            color: white !important; /* Letra negra */
        }
        .stCheckbox .stCheckboxBox {
            background-color: white !important; /* Fondo blanco */
            border-color: white !important; /* Borde negro */
        }
        /* Estilo para el cuadrito interior del checkbox */
        .stCheckbox input[type="checkbox"] {
            background-color: white !important; /* Fondo blanco */
            border-color: white !important; /* Borde negro */
        }
        /* Estilo para los botones */
        .stButton button {
            background-color: #A2E4B8 !important; /* Fondo verde */
            color: white !important; /* Letra blanca */
            border-radius: 5px !important; /* Bordes redondeados */
            border: 1px solid #A2E4B8 !important; /* Borde verde */
            padding: 10px 20px !important; /* Espaciado interno */
        }
        .stButton button:hover {
            background-color: #64AC8F !important; /* Fondo verde oscuro al pasar el cursor */
            border-color: #64AC8F !important; /* Borde verde oscuro al pasar el cursor */
        }
    </style>
    """,
    unsafe_allow_html=True
    )
    
    # Mostrar título y descripción centrados
    st.markdown("""
        <h1 style='text-align: center;color: black;'>Evaluación de Riesgo de Accidente Cerebrovascular</h1>
        <h3 style='text-align: center;color: black; font-size: 20px;'>Por favor complete la encuesta.</h3>
    """, unsafe_allow_html=True)
    
    # Entrada numérica con descripción
    age = st.number_input("Edad del paciente", min_value=0, max_value=120, step=1, help="Ingrese la edad del paciente en años.")
    
    # Selección de género con descripción
    gender = st.radio("Género", ("Masculino", "Femenino"), help="Seleccione el género del paciente.")
    
    # Variables binarias con checkboxes y descripciones
    symptoms = {
        "chest_pain": ("Dolor en el pecho", "Sensación de opresión, presión o ardor en el pecho."),
        "high_blood_pressure": ("Hipertensión arterial", "Presión arterial elevada que puede aumentar el riesgo de un accidente cerebrovascular."),
        "irregular_heartbeat": ("Latidos irregulares", "Sensación de palpitaciones o latidos irregulares en el corazón."),
        "shortness_of_breath": ("Falta de aire", "Dificultad para respirar o sensación de ahogo."),
        "fatigue_weakness": ("Fatiga o debilidad", "Sensación de agotamiento o falta de energía."),
        "dizziness": ("Mareo", "Sensación de inestabilidad o pérdida de equilibrio."),
        "swelling_edema": ("Hinchazón o edema", "Acumulación de líquidos en piernas, tobillos o pies."),
        "neck_jaw_pain": ("Dolor en el cuello o mandíbula", "Malestar en estas zonas que puede estar relacionado con problemas cardiovasculares."),
        "excessive_sweating": ("Sudoración excesiva", "Transpiración abundante sin causa aparente."),
        "persistent_cough": ("Tos persistente", "Tos que no desaparece y puede estar relacionada con problemas cardiovasculares."),
        "nausea_vomiting": ("Náuseas o vómitos", "Sensación de malestar estomacal o ganas de vomitar."),
        "chest_discomfort": ("Malestar en el pecho", "Sensación de incomodidad o presión en el área del pecho."),
        "cold_hands_feet": ("Manos o pies fríos", "Extremidades frías debido a problemas circulatorios."),
        "snoring_sleep_apnea": ("Ronquidos o apnea del sueño", "Interrupciones en la respiración durante el sueño."),
        "anxiety_doom": ("Sensación de ansiedad o presentimiento de fatalidad", "Sensación repentina de angustia sin causa aparente.")
    }
    
    # Creación de checkboxes con descripciones
    symptoms_selected = {}
    for key, (label, description) in symptoms.items():
        symptoms_selected[key] = st.checkbox(label, help=description)
    
    # Botón para obtener los datos ingresados
    if st.button("Predecir Riesgo"): 
        patient_data = {
            "age": age,
            "gender": gender,
            **symptoms_selected
        }
        st.write("Datos del paciente para modelo predictivo:", patient_data)
        
if __name__ == "__main__":
    main()