import os
from pathlib import Path
import pandas as pd

from ConsignmentPricingPrediction.utils.common import load_object, encode_dataset
from ConsignmentPricingPrediction.constants import FEATURE_COLUMNS

class PredicationPipeline:

    def __init__(self, filename):
        self.filename = filename
    
    def load_model(self):
        os.chdir('../')
        # print(os.path.join('artifacts','model_trainer','model.pkl'))
        # model = load_object(path=Path('../../artifacts/model_trainer/model.pkl'))
        model = load_object(path=os.path.join('artifacts','model_trainer','model.pkl'))
        return model
    
    def load_feature_map(self):
        feature_map = load_object(os.path.join("artifacts","data_transformation", "feature_map.pkl"))
        return feature_map

    def load_transform_function(self):
        transform_function = load_object(path= Path(os.path.join("artifacts","data_transformation", "transform_function.pkl")))
        return transform_function
    
    def predict(self):
        # loading the model 
        model = self.load_model()

        # loading the feature map
        feature_map = self.load_feature_map()
        
        # Loading the prediction data 
        transform_function = self.load_transform_function()

        # loading the test data
        test_data = pd.read_csv(self.filename, usecols= FEATURE_COLUMNS)
        transformed_data = transform_function(test_data)

        # encoding the data
        cat_col = transformed_data.select_dtypes(object).columns
        encoded_data = encode_dataset(feature_map, cat_col, transformed_data)

        # Predicting the test data
        predictions = model.predict(encoded_data)
        print(predictions)

        return predictions