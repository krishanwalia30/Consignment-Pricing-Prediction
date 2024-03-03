from ConsignmentPricingPrediction.components.data_transformation import DataTransformation
from ConsignmentPricingPrediction.config.configuration import ConfigurationManager
from ConsignmentPricingPrediction.logging import Logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.transformation()

if __name__ == "__main__":
    STAGE_NAME = "Data Transformation"
    try:
        Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<\n")
    except Exception as e:
        Logger.exception(e)
        raise e
