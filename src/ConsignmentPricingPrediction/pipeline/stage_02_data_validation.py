from ConsignmentPricingPrediction.config.configuration import ConfigurationManager
from ConsignmentPricingPrediction.components.data_validation import DataValidation
from ConsignmentPricingPrediction.logging import Logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.initiate_data_validation()

if __name__ == "__main__":
    STAGE_NAME = "Data Validation"
    try:
        Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<\n")
    except Exception as e:
        Logger.exception(e)
        raise e
