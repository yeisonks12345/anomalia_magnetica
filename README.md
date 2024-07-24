# App para estimar la anomalía magnética en Colombia
Esta aplicacion estima la anomalía magnética en diferentes puntos geolocalizados a partir de 4 variables: Elevation (m),Surface Temperature (C),Moho Depth (m), Curie Depth (Km), los datos fueron tomados a partir del trabajo realizado por Juan C. Mejía Fragoso,  Manuel A. Flórez, Rocío Bernal Olaya en el paper Predicting the geothermal gradient in Colombia: A machine learning approach, para estimar la anomalia se usa un modelo de machine learnig random forest que genera las siguientes métricas: R2 0.90, Mean absolute error: 3.81.""")
# Modelo Random forest
Random Forest es un algoritmo de aprendizaje supervisado que se utiliza tanto para tareas de clasificación como de regresión. Se basa en la construcción de múltiples árboles de decisión durante el entrenamiento y la salida de la clase que es el modo de las clases (clasificación) o la media de las predicciones (regresión) de los árboles individuales.

## Funcionamiento:
Bootstrap Aggregation (Bagging):

Se crean múltiples muestras de entrenamiento mediante muestreo aleatorio con reemplazo del conjunto de datos original.
Cada muestra es usada para entrenar un árbol de decisión individual.
Selección Aleatoria de Características:

Durante la construcción de cada árbol, en cada nodo, se selecciona aleatoriamente un subconjunto de las características en lugar de considerar todas las características.
Esto introduce una mayor diversidad entre los árboles.
## Crecimiento de Árboles:

Cada árbol se crece al máximo posible sin podar.
Al no podar los árboles, se asegura que cada árbol tenga alta varianza y baja sesgo.
## Agregación de Predicciones:

Para la clasificación: se toma la clase que recibe la mayoría de los votos de los diferentes árboles.
Para la regresión: se toma el promedio de las predicciones de los diferentes árboles.
# Indicaciones para usar la app
En la parte izquierda de la aplicación encontrará cuatro barras deslizantes que representan cada varaible del modelo, al modificar las barras, el modelo estimará la anomalía magnética.


# Despliegue en local de la app
Para desplegar la aplicación, clone el repositorio alojado en git hub, posteriormente instale las siguientes librerias que encuentra en el archivo requierements.txt:
1. streamlit
2. pandas
3. numpy
4. pickle

Tenga en cuenta que adicionalmente se debe disponer de el lenguaje de programación python, git bash, para instalar los paquetes que permitiran correr la aplicación en local. 
