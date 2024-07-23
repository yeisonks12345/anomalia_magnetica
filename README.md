# App para estimar la anomalía magnética en Colombia
Esta aplicacion estima la anomalía magnética en diferentes puntos geolocalizados a partir de 4 variables: Elevation (m),Surface Temperature (C),Moho Depth (m), Curie Depth (Km), los datos fueron tomados a partir del trabajo realizado por Juan C. Mejía Fragoso,  Manuel A. Flórez, Rocío Bernal Olaya en el paper Predicting the geothermal gradient in Colombia: A machine learning approach, para estimar la anomalia se usa un modelo de machine learnig random forest que genera las siguientes métricas: R2 0.90, Mean absolute error: 3.81.""")
# Indicaciones para usar la app
En el menú de la izquierda encontrará cuatro barras deslizantes que representan cada varaible del modelo, al modificar las barras, el modelo estimará la anomalía magnética.


# Despliegue en local de la app
Para desplegar la aplicación, clone el repositorio alojado en git hub, posteriormente instale las siguientes librerias que encuentra en el archivo requierements.txt:
1. streamlit
2. pandas
3. numpy
4. pickle

Tenga en cuenta que adicionalmente se debe disponer de el lenguaje de programación python, git bash, para instalar los paquetes que permitiran correr la aplicación en local. 
