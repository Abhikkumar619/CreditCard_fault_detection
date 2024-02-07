import os
import sys
from pathlib import Path
from flask import request
from src.Credit_card_project.config.configuration import PredictConfig
from src.Credit_card_project import logger
import pandas as pd
from src.Credit_card_project.utils.common import load_object


class PredictPipeline:
    def __init__(self, config: PredictConfig): 
        self.config=config
    def save_input_files(self): 
        try: 
            pred_file_input_dir="predction_artifacts"
            os.makedirs(pred_file_input_dir, exist_ok=True)
            
            input_csv_file=self.request.files['file']
            
            pred_file_path=os.path.join(pred_file_input_dir, input_csv_file.filename)
            
            input_csv_file.save(pred_file_path)
            
            return pred_file_path
            
        except Exception as e: 
            raise e
    
    def predict_model(self, input_dataframe): 
        try: 
            model_preprocess=load_object(self.config.preprocess_model)
            logger.info(f"data preprocessing model loaded sucessful")
            preprocess_data=model_preprocess.transfrorm(input_dataframe)
            
            ml_model=load_object(self.config.ml_model)
            pred=ml_model.fit(preprocess_data)
            
            return pred
            
        except Exception as e: 
            
            raise e
    
    
    def get_predicted_dataframe(self, input_dataframe_path: Path):
         
        try: 
            predict_column_name: str="default payment next month"
            input_dataframe=pd.read_csv(input_dataframe_path)
            
            prediction=self.predict_model(input_dataframe)
            
            input_dataframe[predict_column_name]=[pred for pred in prediction]
            
            
            
            
        except Exception as e:
            raise e
    
    def run_pipeline(self): 
        try: 
            input_csv_file=input_csv_file=self.save_input_files()
            logger.info(f" Input csv file saved at {input_csv_file}")
            self.get_predicted_dataframe(Path(input_csv_file))
        except Exception as e: 
            raise e