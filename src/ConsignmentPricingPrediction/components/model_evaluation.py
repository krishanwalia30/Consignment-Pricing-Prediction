from pathlib import Path
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from ConsignmentPricingPrediction.entity import ModelEvaluationConfig
from ConsignmentPricingPrediction.utils.common import load_object
from ConsignmentPricingPrediction.logging import Logger
import yaml

class ModelEvaluation:
    def __init__(self, model_evaluation_config: ModelEvaluationConfig):
        self.config = model_evaluation_config

    def fetch_dataset(self):
        data = pd.read_csv(self.config.test_data_path)
        Logger.info("Test Dataset has been fetched successfully")
        return data
    
    def seperating_dataset(self, testDF: pd.DataFrame):
        x = testDF.drop(columns=[self.config.target_column], axis=1)
        y = testDF[self.config.target_column]

        Logger.info('Test Dataset has been separated successfully')
        return x,y
    
    def scal_dataset(self, testDF: pd.DataFrame):
        scaler = load_object(path= Path(self.config.scaler_path))
        scaled_testDF = scaler.transform(testDF)

        Logger.info('Test Dataset has been scaled successfully')
        return scaled_testDF
    
    def fetch_model(self):
        model = load_object(path= Path(self.config.model_path))

        Logger.info('Trained Model has been fetched successfully')
        return model
    
    
    def save_metrics(self, r2, mae, mse, mape):
        metrics = {
            "R2_Score": float(r2),
            "Mean_Absolute_Error": float(mae),
            "Mean_Squared_Error": float(mse),
            "Mean_Absolute_Percentage_Error": float(mape),
        }

        with open(self.config.metrics_file_path, 'w') as f:
            yaml.dump(metrics, f)
        Logger.info('Trained Metrics has been saved successfully at {}'.format(self.config.metrics_file_path))

    def evaluate_model(self):
        data = self.fetch_dataset()
        x,y =  self.seperating_dataset(data)
        scal_x = self.scal_dataset(x)

        model = self.fetch_model()

        y_pred = model.predict(scal_x)
        Logger.info("Predictions on the testing dataset has been computed")

        r2 = r2_score(y, y_pred)
        mae = mean_absolute_error(y, y_pred)
        mse = mean_squared_error(y,y_pred)
        mape = mean_absolute_percentage_error(y,y_pred)
        Logger.info("Model has been evaluated")
        
        self.save_metrics(r2, mae, mse, mape)
        