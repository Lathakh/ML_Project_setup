import os
import sys
import dill

import pandas as pd
import numpy as np

from src.exception import CustomException

from sklearn.metrics import r2_score



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)  # Get the directory of the file

        # Ensure the directory exists before saving the file
        os.makedirs(dir_path, exist_ok=True)

        # Now save the object using dill
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)  # dill helps serialize the object
            
    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        model_scores = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            score = r2_score(y_test, predictions)
            model_scores[name] = score
    
        return model_scores  # Ensure it returns a dictionary, not None

    except Exception as e:
        raise CustomException(e,sys)    