
from src.Credit_card_project.entity.config_entity import DataValidationConfig
from src.Credit_card_project import logger
import pandas as pd
class DataValidation: 
    def __init__(self, config: DataValidationConfig): 
       self.config=config
    
    def validation_all_column(self): 
        try: 
            validation_state=None
            data=pd.read_csv(self.config.data_path)
            # logger.info(f"Data Loaded: {data.head()}")
            all_columns=list(data.columns)
            logger.info(f"ALL Columns: {all_columns}")
            
            
            all_schema=self.config.all_schema.keys()
            logger.info(f"All Schema: {all_schema}")
            
            for col in all_columns: 
                if col not in all_schema: 
                    Validation_state= False
                    with open(self.config.status_file,'w') as f: 
                        f.write(f"Validation state: {Validation_state}")
                else: 
                    Validation_state= True
                    with open(self.config.status_file,'w') as f: 
                        f.write(f"Validation state: {Validation_state}")
                       
            return Validation_state
                
            
        except Exception as e: 
            raise e
            