from GUI import GUI
from HAL import HAL
import math
import numpy as np
import pandas as pd
import joblib

v_speed = 4.5

model_type = 1
model_name = 'RF_3laps'

def load_model(type):
    if type == 1:
        # Carga el modelo desde el archivo
        model = joblib.load(f'models/{model_name}.pkl')
    else:
        model = None
    
    return model

# Load the model
model = load_model(model_type)
    
# Main loop
while True:
    image = HAL.getImage()
    GUI.showImage(image)
    laser_data = HAL.getLaserData()

    # Remove the inf values from the laser data
    laser_data = np.array(laser_data.values)
    laser_data[laser_data == np.inf] = 20

    # Create a 2D array from the laser data
    laser_data = laser_data.reshape(1, -1)

    # Predict the output
    w_pred = model.predict(laser_data)

    HAL.setV(v_speed)
    HAL.setW(w_pred)
