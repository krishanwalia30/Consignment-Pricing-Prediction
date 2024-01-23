from ConsignmentPricingPrediction.logging import Logger
from ConsignmentPricingPrediction.logging.stage_01_data_ingestion import DataIngestionTrainingPipeline

#################################

STAGE_NAME = "Data Ingestion"
try:
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<")
except Exception as e:
    Logger.exception(e)
    raise e

#################################