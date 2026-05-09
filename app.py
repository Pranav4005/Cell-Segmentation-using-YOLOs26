from src.cellSegmentation.logging import logging
from src.cellSegmentation.exceptions import AppException
import sys
from src.cellSegmentation.pipeline.training_pipeline import TrainPipeline

object = TrainPipeline()
object.run_pipeline()
print("Pipeline execution completed successfully")  