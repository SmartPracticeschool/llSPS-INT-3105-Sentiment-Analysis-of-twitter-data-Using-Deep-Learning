import os

import pickle
#import scipy as sp
#import numpy as np
from tensorflow.keras.models import load_model

def brain(x):
    if not os.path.isfile('./model.h5'): return "Unable to find Saved Model"
    model = load_model('model.h5')
    with open('cv.pkl', 'rb') as file:
        cv = pickle.load(file)
        x = cv.transform([x])
        
        pred = model.predict(x)
        if(pred > 0.5):
            return 1
        else:
            return 0
