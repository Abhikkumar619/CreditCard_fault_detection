
from src.Credit_card_project import logger
from src.Credit_card_project.config.configuration import ConfigurationManager
from src.Credit_card_project.components.data_validation import DataValidation

stage_name= "Data_Validation"

class DataValidationPipeline: 
    def __init__(self):
        pass
    
    def main(self): 
        try: 
            configmanager=ConfigurationManager()
            data_validation_config=configmanager.get_data_validation_config()
            data_validation=DataValidation(data_validation_config)
            data_validation.validation_all_column()
        except Exception as e: 
            raise e
        
if __name__== '__main__': 
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {stage_name} Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Compleated >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e
        