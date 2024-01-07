# 1 Getting preprocessor object 
# 2 GEtting model 
import pandas as pd 
import numpy as np 
from src.utils import load_object 
import os 
import sys

class PredictData:

    def Predict(self,data_to_be_predicted):

        preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
        model_path = os.path.join('artifacts', 'model.pkl')

        preprocessor = load_object(preprocessor_path)
        model = load_object(model_path)

        scaled_data = preprocessor.transform(data_to_be_predicted)
        pred_val = model.predict(scaled_data)

        print(pred_val)
        return pred_val

class CustomData:

    def __init__(self,market_id,
                    store_id,
                    order_protocol,
                    total_items,
                    subtotal,
                    num_distinct_items,
                    total_onshift_dashers,
                    total_busy_dashers,
                    total_outstanding_orders,
                    estimated_order_place_duration,
                    estimated_store_to_consumer_driving_duration,
                    non_null_primary_category,
                    time):
        
        self.market_id = market_id
        self.store_id = store_id
        self.order_protocol = order_protocol
        self.total_items = total_items
        self.subtotal = subtotal
        self.num_distinct_items = num_distinct_items
        self.total_onshift_dashers = total_onshift_dashers
        self.total_busy_dashers = total_busy_dashers
        self.total_outstanding_orders = total_outstanding_orders
        self.estimated_order_place_duration = estimated_order_place_duration
        self.estimated_store_to_consumer_driving_duration = estimated_store_to_consumer_driving_duration
        self.non_null_primary_category = non_null_primary_category
        self.time = time


    def get_data_as_df(self):
        """we are taking user values and converting it to dataframe so... here we provide 
        column names and self.values"""
        dictionary = {
            'market_id' : [self.market_id],
            'store_id' : [self.store_id],
            'order_protocol' : [self.order_protocol],
            'total_items' : [self.total_items],
            'subtotal' : [self.subtotal],
            'num_distinct_items' : [self.num_distinct_items],
            'total_onshift_dashers' : [self.total_onshift_dashers],
            'total_busy_dashers' : [self.total_busy_dashers],
            'total_outstanding_orders' : [self.total_outstanding_orders],
            'estimated_order_place_duration' : [self.estimated_order_place_duration],
            'estimated_store_to_consumer_driving_duration' : [self.estimated_store_to_consumer_driving_duration],
            'non_null_primary_category' : [self.non_null_primary_category],
            'time' : [self.time]
        }

        df = pd.DataFrame(dictionary)
        return df