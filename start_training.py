import os
import sys

from SRC.exception.exception import NetworkSecurityException
from SRC.logger.logger import logging

from SRC.pipeline.training_pipeline import TrainingPipeline


def start_training():
    try:
        logging.info("training has started")

        model_training=TrainingPipeline()
        model_training.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
if __name__=='__main__':
    start_training()