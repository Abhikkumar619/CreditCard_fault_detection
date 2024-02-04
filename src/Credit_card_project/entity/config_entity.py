from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    data_url: Path
    raw_data: Path
    unzip_dir: Path
    
    
@dataclass(frozen=True)
class DataValidationConfig: 
    root_dir: Path
    data_path: Path
    status_file: Path
    all_schema: dict
    
@dataclass(frozen=True)
class DataTransformationConfig: 
    root_dir: Path
    data_dir: Path
    train_data_path: Path
    test_data_path: Path
    test_percentage: float
    target_column: str
    train_scaled: Path
    test_scaled: Path
    
    
from dataclasses import dataclass
@dataclass(frozen=True)
class ModelTrainerConfig: 
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    final_model: Path
    
    