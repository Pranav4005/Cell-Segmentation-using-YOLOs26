import sys
import os

from src.cellSegmentation.logging import logging
from src.cellSegmentation.exceptions import AppException

from src.cellSegmentation.components.data_ingestion import DataIngestion
from src.cellSegmentation.components.data_validation import DataValidation
from src.cellSegmentation.components.model_trainer import ModelTrainer

from src.cellSegmentation.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    ModelTrainerConfig
)

from src.cellSegmentation.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    ModelTrainerArtifact
)


class TrainPipeline:

    def __init__(self):

        self.data_ingestion_config = DataIngestionConfig()

        self.data_validation_config = DataValidationConfig()

        self.model_trainer_config = ModelTrainerConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:

        try:

            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )

            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )

            data_ingestion_artifact = (
                data_ingestion.initiate_data_ingestion()
            )

            logging.info("Got the data from URL")

            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)

    def start_data_validation(
        self,
        data_ingestion_artifact: DataIngestionArtifact
    ) -> DataValidationArtifact:

        logging.info(
            "Entered the start_data_validation method of TrainPipeline class"
        )

        try:

            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config
            )

            data_validation_artifact = (
                data_validation.initiate_data_validation()
            )

            logging.info("Performed data validation")

            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:

        try:

            trained_model_path = (
                self.model_trainer_config.trained_model_file_path
            )

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=trained_model_path
            )

            return model_trainer_artifact

        except Exception as e:
            raise AppException(e, sys)

    def run_pipeline(self) -> None:

        try:

            data_ingestion_artifact = (
                self.start_data_ingestion()
            )

            data_validation_artifact = (
                self.start_data_validation(
                    data_ingestion_artifact=data_ingestion_artifact
                )
            )

            model_trainer_artifact = (
                self.initiate_model_trainer()
            )

        except Exception as e:
            raise AppException(e, sys)


    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            model_trainer_artifact = self.initiate_model_trainer()
        except Exception as e:
            raise AppException(e, sys)
   
