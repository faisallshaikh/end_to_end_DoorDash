# Creating a model 
from dataclasses import dataclass 
import os 
import sys 
from src.exception_file import CustomException 
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from src.utils import evaluate_models, save_object
import logging 


@dataclass
class ModelTrainingConfig:

    model_path = os.path.join('artifacts', 'model.pkl')

class ModelTraining:

    def __init__(self):
        try:

            self.model_training_config = ModelTrainingConfig()

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_model_training(self,transformed_train_data,transformed_test_data):
        logging.info("Initiating Model Training")
        try:

            X_train = transformed_train_data[:,:-1]
            y_train = transformed_train_data[:,-1]
            X_test = transformed_test_data[:,:-1]
            y_test = transformed_test_data[:,-1]

            models = {
                "RandomForestRegressor" : RandomForestRegressor(),
                "GradientBoostingRegressor" : GradientBoostingRegressor()
            }

            params = {}

            train_report, test_report , select_model_report = evaluate_models(
                X_train,X_test,y_train,y_test,models,params
            )


            best_model_score = max(select_model_report.values())

            best_model_name = ""

            for key in select_model_report:
                if select_model_report[key] == best_model_score:
                    best_model_name += key

            best_model = models[best_model_name]

            logging.info("Saving Model...")
            save_object(
                self.model_training_config.model_path,
                best_model
            )

            logging.info("Model saved")

            print(f"Train Data report {train_report} \nTest Data report {test_report} \
                  \nModel Selected {best_model_name} : Score {best_model_score}")
            
            
        except Exception as e:
            raise CustomException(e,sys)