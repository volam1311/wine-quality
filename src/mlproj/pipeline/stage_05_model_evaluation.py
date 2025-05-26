from mlproj.config.configuration import ConfigurationManager
from mlproj.components.model_evaluation import ModelEvaluation
from mlproj import logger

STAGE_NAME = "Data Evaluation stage"
class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()