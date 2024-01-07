from dataclasses import dataclass 
import os 
import sys 
from src.exception_file import CustomException 
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 



@dataclass 
class DataIngestionConfig:

    raw_data_path : str = os.path.join('artifacts', 'raw_data.csv')
    train_data_path : str = os.path.join('artifacts', 'train_data.csv')
    test_data_path : str = os.path.join('artifacts', 'test_data.csv')


class DataIngestion:

    def __init__(self):

         try:
             
             self.data_ingestion_config = DataIngestionConfig()
         
         except Exception as e:
             raise CustomException(e,sys)
         
    def initiate_data_ingestion(self):

        data_path = r'D:\Faisal\Projects\DoorDash\dataset\final_doordash.csv'
        df = pd.read_csv(data_path)

        os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)

        df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
        X_train, X_test = train_test_split(df,test_size=0.2,random_state=42)
        X_train.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
        X_test.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)

        return (
            self.data_ingestion_config.raw_data_path,
            self.data_ingestion_config.train_data_path,
            self.data_ingestion_config.test_data_path
        )

