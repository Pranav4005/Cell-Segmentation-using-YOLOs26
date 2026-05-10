import os
import sys
import shutil

from src.cellSegmentation.logging import logging
from src.cellSegmentation.exceptions import AppException
from src.cellSegmentation.entity.config_entity import DataValidationConfig
from src.cellSegmentation.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataValidationArtifact
)


class DataValidation:

    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig
    ):

        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise AppException(e, sys)

    def validate_all_files(self) -> bool:

        try:
            validation_status = True

            extracted_data_dir = os.path.join(
                self.data_ingestion_artifact.feature_store_path,
                  "dataset"
            )

            all_files = os.listdir(extracted_data_dir)
            print(type(extracted_data_dir))
            print(extracted_data_dir)
            for file in self.data_validation_config.all_required_files:

                if file not in all_files:
                    validation_status = False
                    break

            os.makedirs(
                self.data_validation_config.data_validation_dir,
                exist_ok=True
            )

            with open(
                self.data_validation_config.status_file_path,
                'w'
            ) as f:

                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:

        try:
            validation_status = self.validate_all_files()

            data_validation_artifact = DataValidationArtifact(
                validation_status=validation_status
            )

            if validation_status:
                shutil.copy(
                    self.data_ingestion_artifact.data_zip_file_path,
                    os.getcwd()
                )

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)