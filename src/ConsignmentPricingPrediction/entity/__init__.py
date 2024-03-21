from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: Path
    data_path: Path
    required_files: list

@dataclass(frozen=True)
class DataTransformationConfig:
  root_dir: Path
  data_path: Path
  transform_function_path: Path
  feature_map_path: Path
  train_data_path: Path
  test_data_path: Path
  feature_columns : list

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path 
    train_data_path: Path
    model_path: Path
    scaler_path: Path
    target_column: str