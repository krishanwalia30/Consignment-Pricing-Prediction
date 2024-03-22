from ConsignmentPricingPrediction.logging import Logger
from ConsignmentPricingPrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ConsignmentPricingPrediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from ConsignmentPricingPrediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from ConsignmentPricingPrediction.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from ConsignmentPricingPrediction.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

#################################

STAGE_NAME = "Data Ingestion"
try:
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<\n")
except Exception as e:
    Logger.exception(e)
    raise e

#################################

STAGE_NAME = "Data Validation"
try:
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<\n")
except Exception as e:
    Logger.exception(e)
    raise e

#################################

STAGE_NAME = "Data Transformation"
try:
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<\n")
except Exception as e:
    Logger.exception(e)
    raise e

#################################

STAGE_NAME = "Model Training"
try:
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<\n")
except Exception as e:
    Logger.exception(e)
    raise e

#################################

STAGE_NAME = "Model Evaluation"
try:
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<\n")
except Exception as e:
    Logger.exception(e)
    raise e

#################################