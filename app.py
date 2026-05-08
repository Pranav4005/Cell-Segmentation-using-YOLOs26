from cellSegmentation.logging import logging
from src.cellSegmentation.exceptions import AppException
import sys

logging.info("Starting the application...")

try:
    a=4/'6'
except Exception as e:
    logging.info("An error occurred in the application.")
    raise AppException(e, sys)    