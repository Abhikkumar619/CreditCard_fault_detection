import yaml
import os
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from src.Credit_card_project import logger
import json
import pickle

@ensure_annotations
def read_yaml(yaml_path: Path)->ConfigBox: 
    with open(yaml_path) as yaml_file: 
        content=yaml.safe_load(yaml_file)
    logger.info(f"Yaml file read {yaml_path} successfully") 
        
    return ConfigBox(content)

@ensure_annotations
def create_directories(dir_path: list):
    for path in dir_path: 
        os.makedirs(path, exist_ok=True) 
        logger.info(f"Directories created {dir_path}")
        
@ensure_annotations
def save_json(data: dict, path: Path): 
    with  open(path, 'w') as json_file: 
        json.dump(data, json_file)
    logger.info(f"Json data save at {path} sucessful")
    
    
@ensure_annotations
def load_json(path: Path): 
    with open(path) as json_path:
        content=json.load(json_path)
        
    logger.info(f"Json data loaded from path {path}")
    
@ensure_annotations
def save_binaryFile(path: Path, data: object): 
    with open(path, "wb") as file_path:
        pickle.dump(data,file_path)
        logger.info(f"Binary file saved at {path}")


@ensure_annotations
def save_object(file_path: Path, obj:object):
    try:  
        with open(file_path, "wb") as file_obj: 
            pickle.dump(obj, file_obj)
            
    except Exception as e: 
        raise e

@ensure_annotations   
def load_object(file_path: Path): 
    try: 
        with open(file_path,'rb') as file_obj: 
            return pickle.load(file_obj)
    except Exception as e: 
        raise e   
        
        
@ensure_annotations
def load_binaryFile(path: Path): 
    obj=pickle.load(path)
    logger.info(f"Binary file loaded sucessfully from path {path}")
    return obj
    
    
        
        
    