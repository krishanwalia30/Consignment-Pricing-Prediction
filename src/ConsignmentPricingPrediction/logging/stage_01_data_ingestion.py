from ConsignmentPricingPrediction.components.data_ingestion import DataIngestion
from ConsignmentPricingPrediction.config.configuration import ConfigurationManager
from ConsignmentPricingPrediction.logging import Logger

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.initiate_data_ingestion()


if __name__ == "__main__":
    STAGE_NAME = "Data Ingestion"
    try:
        Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<")
    except Exception as e:
        Logger.exception(e)
        raise e