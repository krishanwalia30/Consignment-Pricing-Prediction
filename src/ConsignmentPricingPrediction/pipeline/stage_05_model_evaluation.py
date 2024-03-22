from ConsignmentPricingPrediction.components.model_evaluation import ModelEvaluation
from ConsignmentPricingPrediction.config.configuration import ConfigurationManager
from ConsignmentPricingPrediction.logging import Logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.evaluate_model()

if __name__ == "__main__":
    STAGE_NAME = "Model Evaluation"
    try:
        Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Initiated <<<<<<<<<<<<")
        model_evaluation = ModelEvaluationTrainingPipeline()
        model_evaluation.main()
        Logger.info(f">>>>>>>>>>>> Stage: {STAGE_NAME} | Completed <<<<<<<<<<<<\n")
    except Exception as e:
        Logger.exception(e)
        raise e