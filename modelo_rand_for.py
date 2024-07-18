import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
# Cargar datos
data = pd.read_csv('data_pre_norm.csv',sep=';')
features = data.iloc[:,:4]
target = data['Magnetic Anomaly (nT)']

# Escalado de las variables con minmax

#scaler = MinMaxScaler()
#features=  scaler.fit_transform(features)

Xtrain,Xtest,Ytrain,Ytest=train_test_split(features,target,test_size=0.2,random_state=2)

# Entrenar el modelo
model = RandomForestRegressor(n_estimators=70, random_state=42)
model.fit(Xtrain, Ytrain)

y_pred = model.predict(Xtest)

mae = mean_absolute_error(Ytest, y_pred)
mse = mean_squared_error(Ytest, y_pred)
r2 = r2_score(Ytest, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R-squared Score:", r2)

# Guardar el modelo
with open('random_forest_model.pkl', 'wb') as file:
    pickle.dump(model, file)


"""
Métricas del modelo
Mean Absolute Error: 3.817
Mean Squared Error: 135.89
R-squared Score: 0.90
"""