from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from ConsignmentPricingPrediction.entity import ModelTrainerConfig
from ConsignmentPricingPrediction.utils.common import save_object
from sklearn.metrics import r2_score
from ConsignmentPricingPrediction.logging import Logger

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.config = model_trainer_config

    def fetch_train_data(self)-> pd.DataFrame:
        testDF = pd.read_csv(self.config.train_data_path)
        Logger.info('Training Dataset has been fetched successfully')
        return testDF
    
    def separating_train_data(self, testDF: pd.DataFrame):
        """
        Separating the training data into dependent and independent features
        
        Args:
            testDF: pd.DataFrame
        
        Returns:
            x: pd.DataFrame
            y: pd.DataFrame
        """
        x = testDF.drop(self.config.target_column, axis=1)
        y = testDF[self.config.target_column]
        Logger.info("Dataset has been seperated into dependent and independent features")

        return x, y
    
    def scal_dataset(self, testDF: pd.DataFrame):
        """
        Scale the dataset and then save the scaler

        Args:
            testDF: pd.DataFrame

        Returns:
            scaled_data: ndarray
        """
        scal = StandardScaler()
        scaled_data = scal.fit_transform(testDF)
        Logger.info("Dataset has been scaled successfully")

        # Saving the scaler
        save_object(path=Path(self.config.scaler_path),obj=scal)    
        Logger.info("Scaler has been saved successfully")

        return scaled_data

        
    def training_model(self, x, y):
        models = {
            'LinearRegression': LinearRegression(),
            'Lasso': Lasso(),
            'Ridge': Ridge(),
            'DecisionTree': DecisionTreeRegressor(),
            'RandomForest': RandomForestRegressor(),
        }

        model_accuracy_dict = {}

        for model in models.items():
            # Fitting the model
            model[1].fit(x, y) 
            
            # Testing the accuracy on the training data
            y_pred = model[1].predict(x)
            model_accuracy_dict[model[0]] = r2_score(y,y_pred)

        max_accuracy_score = (max(model_accuracy_dict.values()))
        max_accuracy_model = list(model_accuracy_dict.items())[list(model_accuracy_dict.values()).index(max_accuracy_score)][0]
        Logger.info("Model: {} | Model Accuracy: {}".format(max_accuracy_model, max_accuracy_score))

        final_model = models[max_accuracy_model]
        Logger.info("Model has been trained successfully")
        return final_model

    def save_model(self, model):
        save_object(path=Path(self.config.model_path),obj=model)
        Logger.info("Model has been saved successfully")

    def trainer(self):
        # Fetching the dataset
        data = self.fetch_train_data()

        # Separating the dataset
        x, y = self.separating_train_data(data)

        # Scaling the dataset
        x_scaled = self.scal_dataset(x)

        # Training the model
        model = self.training_model(x_scaled, y)
        
        # Saving the model
        self.save_model(model)