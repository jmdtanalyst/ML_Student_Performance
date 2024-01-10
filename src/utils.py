# utils will hold all common routines for the hole application

import os
import sys
import numpy as np
import pandas as pd
import dill


from src.exception import CustomException
from src.logger import logging

# Function save_object will use dill.dump to save the object on the file path
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    
    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
