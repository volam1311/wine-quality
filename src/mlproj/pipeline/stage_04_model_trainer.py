from mlproj.config.configuration import ConfigurationManager
from mlproj.components.model_trainer import ModelTrainer
from mlproj import logger

STAGE_NAME = "Data Validation stage"
class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()