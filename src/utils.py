import os
import sys
import numpy as np 
import pandas as pd
import stat
import dill
import pickle

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging

def save_object(file_path,obj):
    try:
        # Define the desired permissions (e.g., read, write, and execute for the owner)
         # Owner has read, write, and execute permissions

        # Change the directory permissions
        
        dir_path = os.path.dirname(file_path)
        # permissions = stat.S_IRWXU
        # os.chmod(dir_path, permissions)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj) 
        
        
    except Exception as e:
        raise CustomException(e,sys)