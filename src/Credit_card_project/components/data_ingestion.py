from urllib.request import urlretrieve
from src.Credit_card_project import logger
import zipfile
from src.Credit_card_project.entity.config_entity import DataIngestionConfig
from src.Credit_card_project import logger
import os


class DataIngestion: 
    def __init__(self, config: DataIngestionConfig): 
        self.config=config
        
    def download_data(self):
        if not os.path.exists(self.config.raw_data): 
            file_name, header=urlretrieve(url=self.config.data_url, filename=self.config.raw_data)
            logger.info(f"data download file name: {file_name}, hader: {header}")
        else: 
            logger.info(f"Data is already exists {self.config.raw_data}")
    
    def UnZipFile(self): 
        unfile_path=self.config.root_dir
        with zipfile.ZipFile(self.config.raw_data,'r') as zip_r: 
            zip_r.extractall(unfile_path)