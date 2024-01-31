from src.Credit_card_project.config.configuration import ConfigurationManager
from src.Credit_card_project.components.data_ingestion import DataIngestion
from src.Credit_card_project import logger


stage="Data_Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self): 
        try: 
            configmanager=ConfigurationManager()
            dataingestion_config=configmanager.get_data_ingestion_config()
            dataingestion=DataIngestion(dataingestion_config)
            dataingestion.download_data()
            dataingestion.UnZipFile()
        except Exception as e: 
            raise e
        
        
if __name__ == "__main__": 
    try: 
        logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage} Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e
        
        