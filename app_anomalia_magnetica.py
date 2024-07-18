import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
#configurar pagina streamlit

st.set_page_config(page_title="App anomalia magnetica",
                   layout="centered",
                   initial_sidebar_state="auto")

#definimos titulo
st.title("Estimación de anomalía magnética en Colombia, a partir de un modelo de machine learning Random Forest")
st.markdown(""" Esta aplicacion estima la anomalía magnética en diferentes puntos geolocalizados a partir de 4 variables: Elevation (m),Surface Temperature (C),Moho Depth (m), Curie Depth (Km), los datos fueron tomados a partir del trabajo realizado por Juan C. Mejía Fragoso,  Manuel A. Flórez, Rocío Bernal Olaya en el paper Predicting the geothermal gradient in Colombia: A machine learning approach, para estimar la anomalia se usa un modelo de machine learnig random forest que genera las siguientes métricas: R2 0.90, Mean absolute error: 3.81.""")
st.sidebar.header("Datos suministrados por el usuario")
def user_input_features():
    Elevation = st.sidebar.slider('Elevación en metros',0,3116,2000)
    Surface_temperature = st.sidebar.slider('Elevación en metros',12,28,15)
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
st.write("con base en los parametros escogidos la anomalía magnética se estima en:")
st.write(prediction)




