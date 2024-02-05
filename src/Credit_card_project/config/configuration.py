from src.Credit_card_project.utils.common import read_yaml,create_directories
from src.Credit_card_project.constant import *
from src.Credit_card_project.entity.config_entity import DataIngestionConfig
from src.Credit_card_project.entity.config_entity import DataValidationConfig
from src.Credit_card_project.entity.config_entity import DataTransformationConfig
from src.Credit_card_project.entity.config_entity import ModelTrainerConfig

class ConfigurationManager: 
    def __init__(self,config_file_path= CONFIG_FILE_PATH,
                 params_file_path= PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH
                 ):
        self.config=read_yaml(config_file_path)
        self.sparams=read_yaml(params_file_path)
        self.schema=read_yaml(schema_file_path)
        
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        
        config= self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            data_url=config.data_url,
            raw_data=config.raw_data,
            unzip_dir=config.unzip_dir)
        
        return data_ingestion_config
    
    def get_data_validation_config(self)-> DataValidationConfig: 
        
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        create_directories([config.root_dir])
        
        data_validation_config=DataValidationConfig(
            root_dir= config.root_dir, 
            data_path=config.data_path,
            status_file=config.status_file,
            all_schema=schema)
        return data_validation_config
    
    def get_data_transformation_config(self)-> DataTransformationConfig:
        
        config= self.config.data_transformation
        schema=self.schema.TARGET
        create_directories([config.root_dir])
        
        get_data_transformation_config=DataTransformationConfig(
                root_dir=config.root_dir,
                data_dir=config.data_dir,
                test_data_path=config.test_data_path,
                train_data_path=config.train_data_path,
                test_percentage=config.test_percentage,
                target_column=schema, 
                train_scaled=config.train_scaled,
                test_scaled=config.test_scaled,
                preprocess_path=config.model_path
                
                
            )
        return get_data_transformation_config
        
    def get_model_trainer_config(self)-> ModelTrainerConfig: 
            
            config=self.config.model_trainer
            schema=self.schema.COLUMNS

            create_directories([config.root_dir])
            
            model_train_config=ModelTrainerConfig(
                root_dir=config.root_dir,
                train_data_path=config.train_data_path,
                test_data_path=config.test_data_path,
                final_model=config.Final_model)
            
            return model_train_config
        
        