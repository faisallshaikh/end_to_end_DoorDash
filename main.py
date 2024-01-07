import sys 
from src.exception_file import CustomException 
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation 
from src.components.model_trainer import ModelTraining 


if __name__ == '__main__':

    try :

        data_ingestion = DataIngestion()
        raw_data, train_data,test_data = data_ingestion.initiate_data_ingestion()

        data_transform = DataTransformation()
        transformed_train_data,transformed_test_data,_ = data_transform.initiate_data_transformation(raw_data)

        model_trainer = ModelTraining()
        model_trainer.initiate_model_training(transformed_train_data,transformed_test_data)
                

    except Exception as e:
        raise CustomException(e,sys)