import os
import urllib.request as request
import zipfile
from pathlib import Path
from chicken_disease_classification import logger
from chicken_disease_classification.utils.common import get_size
from chicken_disease_classification.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    def download_data(self) -> Path:
        logger.info("Starting data download...")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(
                f"File: {filename} downloaded with info: {headers} and size: {get_size(Path(filename))}"
            )
        else:
            logger.info(f"File already exists of size: {get_size(self.config.local_data_file)}")
        return self.config.local_data_file
    def extract_zip_file(self, zip_file_path: Path):
        logger.info("Starting data extraction...")
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info(f"Data extracted at location: {self.config.unzip_dir}")