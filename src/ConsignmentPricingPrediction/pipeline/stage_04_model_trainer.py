from ConsignmentPricingPrediction.components.model_trainer import ModelTrainer
from ConsignmentPricingPrediction.config.configuration import ConfigurationManager
from ConsignmentPricingPrediction.logging import Logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.trainer()

if __name__ == "__main__":
    STAGE_NAME = "Model Training"
    try:
        Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
        model_trainer = ModelTrainerTrainingPipeline()
        model_trainer.main()
        Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<\n")
    except Exception as e:
        Logger.exception(e)
        raise e