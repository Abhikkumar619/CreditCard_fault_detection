from src.Credit_card_project.config.configuration import ConfigurationManager
from src.Credit_card_project.components.Model_Trainer import ModelTrainer
from src.Credit_card_project import logger


stage_name="Model_Trainer"
class ModelTrainerPipeline: 
    def __init__(self):
        pass
    def main(self):
        try: 
            configmanager=ConfigurationManager()
            get_model_config=configmanager.get_model_trainer_config()
            model_trainer=ModelTrainer(get_model_config)
            model_trainer.initiate_model_trainer()
        except Exception as e:
            raise e
        
if __name__ == "__main__": 
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {stage_name} started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e  