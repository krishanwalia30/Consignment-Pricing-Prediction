import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from ConsignmentPricingPrediction.entity import DataTransformationConfig

from ConsignmentPricingPrediction.utils.common import *

class DataTransformation:
    def __init__(
            self,
            config: DataTransformationConfig
            ):
        self.config = config
    
    def fetch_dataset(self):
        testDF = pd.read_csv(self.config.data_path, usecols=self.config.feature_columns)
        return testDF

    def save_split_dataset(self, testDF: pd.DataFrame):
        train, test = train_test_split(testDF, random_state=42)     
        train.to_csv(self.config.train_data_path, index=False)
        test.to_csv(self.config.test_data_path, index=False)
    
    def transform_dataset(self, testDF: pd.DataFrame):
        # Droping the na values from the dataframe
        testDF=testDF.dropna()

        # Checking the object values in the Weight Column
        to_drop_weight= []
        for i in testDF['Weight (Kilograms)']: 
            try:
                float(i)
            except:
                to_drop_weight.append(i)
        # Dropping the object values from the Weight Column
        testDF = testDF[testDF['Weight (Kilograms)'].isin(to_drop_weight)==False]

        # Checking the object values in the Freight Column
        to_drop= []
        for i in testDF['Freight Cost (USD)']:
            try:
                float(i)
            except:
                to_drop.append(i)        
                
        # Dropping the object values from the Freight Column
        testDF = testDF[testDF['Freight Cost (USD)'].isin(to_drop)==False]

        # Splitting the scheduled Delivery date column to three respective columns storing the date, month and year
        testDF['Scheduled_Delivery_Date_D'] = [i.split('-')[0] for i in testDF['Scheduled Delivery Date']]
        testDF['Scheduled_Delivery_Date_M'] = [i.split('-')[1] for i in testDF['Scheduled Delivery Date']]
        testDF['Scheduled_Delivery_Date_Y'] = [i.split('-')[2] for i in testDF['Scheduled Delivery Date']]

        # Splitting the delivered to client date column to three respective columns storing the date, month and year
        testDF['Delivered_to_Client_Date_D'] = [i.split('-')[0] for i in testDF['Delivered to Client Date']]
        testDF['Delivered_to_Client_Date_M'] = [i.split('-')[1] for i in testDF['Delivered to Client Date']]
        testDF['Delivered_to_Client_Date_Y'] = [i.split('-')[2] for i in testDF['Delivered to Client Date']]

        # Dropping the columns: Delivered to Client Date, Scheduled Delivery Date and Delivery Recorded Date
        testDF = testDF.drop(columns=['Delivered to Client Date', 'Scheduled Delivery Date','Delivery Recorded Date'], axis= 1)

        # Changing the datatype of the columns
        testDF['Weight (Kilograms)'] = testDF['Weight (Kilograms)'].astype(float)
        testDF['Freight Cost (USD)'] = testDF['Freight Cost (USD)'].astype(float)
        testDF['Scheduled_Delivery_Date_D'] = testDF['Scheduled_Delivery_Date_D'].astype(float)
        testDF['Scheduled_Delivery_Date_Y'] = testDF['Scheduled_Delivery_Date_Y'].astype(float)
        testDF['Delivered_to_Client_Date_D'] = testDF['Delivered_to_Client_Date_D'].astype(float)
        testDF['Delivered_to_Client_Date_Y'] = testDF['Delivered_to_Client_Date_Y'].astype(float)
        
        return testDF
    
    def create_feature_map(self, testDF: pd.DataFrame):
        """
        create a feature map for the given dataset

        Args:
            testDF: pd.DataFrame

        Returns:
            feature_map: dict
            cat_col: list
        """
        cat_col = testDF.select_dtypes(object).columns
        feature_map = {}
        for i in cat_col:
            feature_map[i] = testDF[i].unique()
        
        return feature_map, cat_col

    
    def save_preprocessing_items(self):
        save_object(self.config.transform_function_path, self.transform_dataset)

    def transformation(self):
        """
        Need data for transformation
        split the dataset into training and testing
        transform the dataset
        create a feature map and then save it
        call the feature map 
        pass the feature map into an encoding function
        save the training data that has been encoded 
        save the testing data that has been encoded
        """

        # Fetching the dataset
        df = self.fetch_dataset()

        # Transforming the dataset
        df = self.transform_dataset(df)

        # Saving the transform function
        save_object(path = Path(self.config.transform_function_path), obj = self.transform_dataset)

        # Creating the feature map
        feature_map, cat_col = self.create_feature_map(df)

        # Saving the feature map
        save_object(path = Path(self.config.feature_map_path),obj = feature_map)
        
        # Encoding the dataset
        encoded_df = encode_dataset(feature_map, cat_col, df)

        # Saving the encoded dataset
        self.save_split_dataset(encoded_df)    