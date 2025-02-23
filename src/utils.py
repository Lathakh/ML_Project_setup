import os
import sys
import dill

import pandas as pd
import numpy as np

from src.exception import CustomException



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