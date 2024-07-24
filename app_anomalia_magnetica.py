import streamlit as st
import pandas as pd
import numpy as np
import pickle

#configurar pagina streamlit

st.set_page_config(page_title="App anomalia magnetica",
                   layout="centered",
                   initial_sidebar_state="auto")

#definimos titulo
st.title("Estimación de anomalía magnética en Colombia, a partir de un modelo de machine learning Random Forest")
st.markdown(""" Esta aplicacion estima la anomalía magnética en diferentes puntos geolocalizados a partir de 4 variables: Elevation (m),Surface Temperature (C),Moho Depth (m), Curie Depth (Km), los datos fueron tomados a partir del trabajo realizado por Juan C. Mejía Fragoso,  Manuel A. Flórez, Rocío Bernal Olaya en el paper Predicting the geothermal gradient in Colombia: A machine learning approach, para estimar la anomalia se usa un modelo de machine learnig random forest que genera las siguientes métricas: R2 0.90, Mean absolute error: 3.81.""")
st.title('Modelo random forest')
st.write("Random Forest es un algoritmo de aprendizaje supervisado que se utiliza tanto para tareas de clasificación como de regresión. Se basa en la construcción de múltiples árboles de decisión durante el entrenamiento y la salida de la clase que es el modo de las clases (clasificación) o la media de las predicciones (regresión) de los árboles individuales.")
st.write("Funcionamiento: Bootstrap Aggregation (Bagging): Se crean múltiples muestras de entrenamiento mediante muestreo aleatorio con reemplazo del conjunto de datos original. Cada muestra es usada para entrenar un árbol de decisión individual. Selección Aleatoria de Características: Durante la construcción de cada árbol, en cada nodo, se selecciona aleatoriamente un subconjunto de las características en lugar de considerar todas las características. Esto introduce una mayor diversidad entre los árboles.")
st.title("Indicaciones de uso")
st.write("En la sección lateral de la izquierda se encuentra cuatro barras deslizantes que representan cada variable del modelo (elevación en metros, temperatura de la superficie, profundidad moho en metros, curie deepth). Al modificar las barras, el modelo estimará la anomalía magnética y se podrá visualizar en el recuadro Value.")
st.sidebar.header("Datos suministrados por el usuario")
def user_input_features():
    Elevation = st.sidebar.slider('Elevación en metros',0,3116,2000)
    Surface_temperature = st.sidebar.slider('Temperatura de la superficie',12,28,15)
    Moho = st.sidebar.slider('Profundidad moho en m.',27560,48790,30000)
    curie_deepth = st.sidebar.slider('curie deepth km',10,38,15)
    data ={"Elevation (m)":Elevation,
            "Surface Temperature (C)":Surface_temperature,
            "Moho Depth (m)": Moho,
            "Curie Depth (Km)":curie_deepth
           }
    features = pd.DataFrame(data,index=[0])
    return features
input_df = user_input_features()

st.write("Datos ingresados")
st.write(input_df)
load_clf =pickle.load(open('random_forest_model.pkl','rb'))

prediction = load_clf.predict(input_df)


highlight_css = """
<div style="
    border: 2px solid #4CAF50; 
    padding: 10px; 
    border-radius: 10px; 
    background-color: #f9f9f9; 
    text-align: center; 
    font-size: 24px; 
    font-weight: bold; 
    color: #4CAF50;
">
    {0}
</div>
"""

# Mostrar el dato enmarcado y resaltado

st.write("con base en los parametros escogidos la anomalía magnética se estima en:")
st.markdown(highlight_css.format(prediction[0]), unsafe_allow_html=True)





