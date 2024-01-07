from src.exception_file import CustomException 
import os 
import sys 
import pickle 
from src.logger import logging
from sklearn.metrics import r2_score , mean_absolute_error , mean_squared_error
import numpy as np 
import pandas as pd 


def save_object(file_path, object_file):
    logging.info("Creating pickle file")
    try:
        
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path, 'wb') as f:
            pickle.dump(object_file, f)
            logging.info("Pickle file created")

    except Exception as e:
        logging.info("pickle file not created")
        raise CustomException(e,sys)


def evaluate_models(X_train,X_test,y_train,y_test,models,params):
    logging.info("Evaluating Model")
    try:
        select_model = {}
        train_dict = {}
        test_dict = {}

        for i in range(len(list(models.keys()))):
            model = list(models.values())[i]
            model.fit(X_train,y_train)

            train_preds = model.predict(X_train)
            test_preds = model.predict(X_test)

            r2_train = r2_score(y_train,train_preds)
            r2_test = r2_score(y_test, test_preds)

            MAE_train = mean_absolute_error(y_train,train_preds)
            MAE_test = mean_absolute_error(y_test, test_preds)

            RMSE_train = np.sqrt(mean_squared_error(y_train,train_preds))
            RMSE_test = np.sqrt(mean_squared_error(y_test, test_preds))

            inner_train_dict = {}
            inner_test_dict = {}

            inner_train_dict["r2_score"] = r2_train
            inner_train_dict["MAE"] = MAE_train
            inner_train_dict["RMSE"] = RMSE_train

            inner_test_dict["r2_score"] = r2_test
            inner_test_dict["MAE"] = MAE_test
            inner_test_dict["RMSE"] = RMSE_test

            train_dict[list(models.keys())[i]] = inner_train_dict
            test_dict[list(models.keys())[i]] = inner_test_dict

            select_model[list(models.keys())[i]] = r2_test

            logging.info("Scores Collected")

        return(
                train_dict,
                test_dict,
                select_model
            )
            

    except Exception as e:
        raise CustomException(e,sys)
    

def load_object(file_path):

    try:

        with open(file_path, 'rb') as f:
            return pickle.load(f)

    except Exception as e:
        raise CustomException(e ,sys)

