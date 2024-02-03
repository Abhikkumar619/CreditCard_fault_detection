from src.Credit_card_project import logger
from src.Credit_card_project.config.configuration import ConfigurationManager
from src.Credit_card_project.components.data_transformation import DataTransformation

stage_name= "Data Transformation"
class DataTransformationPipeline: 
    def __init__(self): 
        pass
    def main(self): 
        try:
            configmanager=ConfigurationManager()
            data_transformation_config=configmanager.get_data_transformation_config()
            data_transformation=DataTransformation(data_transformation_config)
            data_transformation.data_transformation_initiate()
        except Exception as e: 
            raise e
        
if __name__ == '__main__': 
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {stage_name} started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e  