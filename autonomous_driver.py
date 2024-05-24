from GUI import GUI
from HAL import HAL
import math
import numpy as np
import pandas as pd
import joblib
import tensorflow
from tensorflow import keras

v_speed = 4.5

model_type = 1
num_samples = ''
scalerName = f''
shuffle = ''
model_name = f'RF{num_samples}_{scalerName}_{shuffle}'

scaler_type = 0

def load_scaler(scaler_type):
    # Carga el modelo desde el archivo
    if(scaler_type == 1):
        scaler = joblib.load('scalers/StandardScaler.joblib')
    elif(scaler_type == 2):
        scaler = joblib.load('scalers/MinMaxScaler.joblib')
    else:
        scaler = None

def load_model(type):
    if type == 1:
        # Carga el modelo desde el archivo
        model = joblib.load(f'models/{model_name}.pkl')
    else:
        model = keras.saving.load_model(f'models/{model_name}.h5')
    
    return model

# Load the model
model = load_model(model_type)
# Load the scaler
scaler = load_scaler(scaler_type)
    
# Main loop
while True:
    image = HAL.getImage()
    GUI.showImage(image)
    laser_data_raw = HAL.getLaserData()

    laser_data_array = np.array(laser_data_raw.values)
    # Remove the inf values from the laser data
    laser_data_array[laser_data_array == np.inf] = 20

    #laser_data = pd.DataFrame([laser_data_array.flatten()], columns=[f'laser_{i}' for i in range(len(laser_data_array))])
    # Create a 2D array from the laser data
    laser_data = laser_data_array.reshape(1, -1)

    # Scale the data
    if scaler is not None:
        laser_data = scaler.transform(laser_data)
        
    # Predict the output
    w_pred = model.predict(laser_data)

    HAL.setV(v_speed)
    HAL.setW(w_pred)
