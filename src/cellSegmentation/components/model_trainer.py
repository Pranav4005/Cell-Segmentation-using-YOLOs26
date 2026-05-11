import os
import sys

from ultralytics import YOLO

from src.cellSegmentation.logging import logging
from src.cellSegmentation.exceptions import AppException
from src.cellSegmentation.entity.config_entity import ModelTrainerConfig
from src.cellSegmentation.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:

    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig
    ):

        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:

        try:

            logging.info("Starting model training")

            # Load pretrained model
            model = YOLO(
                self.model_trainer_config.weight_name
            )

            # Train model
            model.train(
                data=self.model_trainer_config.data_yaml_path,
                epochs=self.model_trainer_config.no_epochs,
                imgsz=640
            )

            os.makedirs(
                self.model_trainer_config.model_trainer_dir,
                exist_ok=True
            )

            trained_model_path = (
                "artifacts/model_trainer/best.pt"
            )

            logging.info("Model training completed")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=trained_model_path
            )

            return model_trainer_artifact

        except Exception as e:
            raise AppException(e, sys)