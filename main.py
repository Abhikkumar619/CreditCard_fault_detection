from src.Credit_card_project import logger

from src.Credit_card_project.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from src.Credit_card_project.pipeline.stage_2_data_validation import DataValidationPipeline
from src.Credit_card_project.pipeline.stage_3_data_transformation import DataTransformationPipeline
from src.Credit_card_project.pipeline.stage_4_model_trainer import ModelTrainerPipeline

"""
stage="Data_Ingestion"

if __name__ == "__main__": 
    try: 
        logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage} Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e
        

stage_name= "Data_Validation"

if __name__ == "__main__": 
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {stage_name} Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Compleated >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e
"""
stage_name= "Data Transformation"

try: 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {stage_name} started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e: 
    raise e  

stage_name="Model_Trainer"
try: 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {stage_name} started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e: 
    raise e  
        
        