from src.Credit_card_project import logger

from src.Credit_card_project.pipeline.stage_1_data_ingestion import DataIngestionPipeline

stage="Data_Ingestion"

if __name__ == "__main__": 
    try: 
        logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage} Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e
        
        