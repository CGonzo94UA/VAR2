from GUI import GUI
from HAL import HAL
import math
import numpy as np
import pandas as pd
import joblib

v_speed = 4.5

model_type = 1


def load_model(type):
    if type == 1:
        # Carga el modelo desde el archivo
        model = joblib.load('random_forest_model.pkl')
    else:
        model = None
    
    return model
    
# Main loop
while True:
    laser_data = HAL.getLaserData()

    # Remove the inf values from the laser data
    laser_data = np.array(laser_data)
    laser_data[laser_data == np.inf] = 20

    # Load the model
    model = load_model(model_type)

    # Predict the output
    w_pred = model.predict(laser_data)

    HAL.setV(v_speed)
    HAL.setW(w_pred)
