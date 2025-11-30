from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.data_ingestion import DataIngestion
from chicken_disease_classification import logger
from pathlib import Path

from chicken_disease_classification.utils.common import create_directories

STAGE_NAME = "Data Ingestion Stage"
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
    
    # Create required directories using your utility function
        create_directories([
        Path(data_ingestion_config.local_data_file).parent,
        Path(data_ingestion_config.unzip_dir)
    ])
    
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file(zip_file_path=data_ingestion_config.local_data_file)
    
    
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e