from ConsignmentPricingPrediction.entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelTrainerConfig
from ConsignmentPricingPrediction.utils.common import read_yaml, create_directories
from ConsignmentPricingPrediction.constants import *

class ConfigurationManager:
    def __init__(
            self,
            config_file_path = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH,
            ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion 

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir,
        )
        return data_ingestion_config
        
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation 

        create_directories([config.root_dir])
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            status_file = config.status_file,
            data_path = config.data_path,
            required_files = config.required_files
        )

        return data_validation_config

    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation 
        params = self.params

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
            transform_function_path= config.transform_function_path,
            feature_map_path= config.feature_map_path,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            feature_columns= params.FEATURE_COLUMNS
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer 
        params = self.params

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path= config.train_data_path,
            model_path= config.model_path,
            scaler_path= config.scaler_path,
            target_column= params.TARGET_COLUMN
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            test_data_path = config.test_data_path,
            model_path = config.model_path,
            scaler_path = config.scaler_path,
            metrics_file_path = config.metrics_file_path,
            target_column = params.TARGET_COLUMN,
        )
        return model_evaluation_config