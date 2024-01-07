from  dataclasses import dataclass 
import os 
import sys 
from src.exception_file import CustomException 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import OneHotEncoder, PowerTransformer, TargetEncoder
from sklearn.compose import ColumnTransformer 
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline 
from category_encoders import BaseNEncoder 
import numpy as np 
import pandas as pd 
from src.logger import logging 
from src.utils import save_object 



@dataclass 
class DataTransformationConfig:

    preprocessor_object_path : str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation: # saving preprocessor object and returning transformed data 

    def __init__(self):
        logging.info("Starting...")
        try:
            logging.info("Initializing....")
            self.data_transformation_config = DataTransformationConfig()  

        except Exception as e:
            raise CustomException(e,sys)

    def get_preprocessor_object(self):
        logging.info("Preparing Transformation/Preprocessor Object")
        try:

            power_features = ['total_items', 'subtotal',
              'num_distinct_items', 'total_onshift_dashers', 'total_busy_dashers',
                'total_outstanding_orders', 'estimated_order_place_duration',
                'estimated_store_to_consumer_driving_duration',
                'store_id']
            
            power_encoder = Pipeline(steps=[
                ("power", PowerTransformer(method='yeo-johnson'))
            ])

            target_feature = ["non_null_primary_category"]

            target_encoder = Pipeline(steps=[
                ("target", TargetEncoder(cv=5, smooth = 5000, target_type = 'continuous'))
            ])

            base_N_features = ["time"]

            base_N_encoder = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy = 'most_frequent')),
                ("base_N", BaseNEncoder(base=4))
            ])

            one_hot_features = ['order_protocol','market_id']

            one_hot_encoder = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy = 'most_frequent')),
                ("one_hot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
            ])


            CT = ColumnTransformer(transformers=[
                ("power", power_encoder,power_features),
                ("target", target_encoder,target_feature),
                ("base_N", base_N_encoder,base_N_features),
                ("one_hot", one_hot_encoder,one_hot_features)
            ],remainder='passthrough')

            preprocessor = Pipeline(steps=[("transform", CT)])

            logging.info("Transformation Object Created")
            return preprocessor
            
        
        except Exception as e :
            logging.info("Tansformation object creation could not be completed")
            raise CustomException(e,sys)
        

    def initiate_data_transformation(self,df_file):
        logging.info("Initializing Data Transformation")
        try:

            df = pd.read_csv(df_file)
            print(df.head())

            X = df.drop("delivery_time",axis=1)
            y = df["delivery_time"]


            X_train,X_test,y_train,y_test = train_test_split(
                X,y,test_size=0.2,random_state=42)
            
            preprocessor_object = self.get_preprocessor_object()

            transformed_X_train = preprocessor_object.fit_transform(X_train,y_train) # need y_train as well for taraget encoding
            transaformed_X_test = preprocessor_object.transform(X_test)

            transformed_train_data = np.c_[transformed_X_train,y_train]
            transformed_test_data = np.c_[transaformed_X_test, y_test]

            save_object(

                self.data_transformation_config.preprocessor_object_path,
                preprocessor_object
            )
            logging.info("Transformation Object saved")

            return (
                transformed_train_data,
                transformed_test_data,
                self.data_transformation_config.preprocessor_object_path
            )

        except Exception as e:
            logging.info("Data Transformation interrupted")
            raise CustomException(e,sys)

        


