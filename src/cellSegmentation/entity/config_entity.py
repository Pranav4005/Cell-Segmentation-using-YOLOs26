import os
from dataclasses import dataclass
from datetime import datetime
from src.cellSegmentation.constants.training_pipeline import *

@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str=ARTIFACTS_DIR


training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir:str= os.path.join(training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME)
    feature_store_dir: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)
    data_download_url: str = DATA_DOWNLOAD_URL

@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME)
    status_file_path: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)
    all_required_files = DATA_VALIDATION_ALL_REQUIRED_FILES    

@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR_NAME)
    weight_name: str = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME
    no_epochs: int = MODEL_TRAINER_NO_EPOCHS
    trained_model_file_path: str = os.path.join(model_trainer_dir, "best.pt")