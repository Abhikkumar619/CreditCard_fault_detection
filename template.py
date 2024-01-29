from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s : %(message)s]")


project_name="Credit_card_project"


list_of_file=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py"
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "application.py",
    "main.py",
    "requirement.txt",
    "setup.py",
    "research/Experiment.ipynb",
    "templates/index.html"
    
]

for path in list_of_file:
    dir_name, file_name=os.path.split(path)
    logging.info(f"directory name: {dir_name}, file_name: {file_name}")
    
    if dir_name != "":
        os.makedirs(dir_name, exist_ok=True)
        logging.info(f"Directory is created for {dir_name} for file {file_name}")
        
    if (not os.path.exists(path) or os.path.getsize(path)==0):
        with open(path, 'w') as f:
            pass
        logging.info(f"Path is created {path}")
        
    else: 
        logging.info(f"{path}  is already created")