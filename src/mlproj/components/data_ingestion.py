import os
import zipfile
import urllib.request as request
from mlproj import logger
from mlproj.utils.common import get_size
from mlproj.entity.config_entity import DataIngestionConfig
import requests
from pathlib import Path
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            response = requests.get(self.config.source_URL)
            
            if 'zip' not in response.headers.get('Content-Type', ''):
                raise ValueError("Downloaded file is not a zip file. Content-Type: " +
                                 response.headers.get('Content-Type', 'unknown'))

            with open(self.config.local_data_file, 'wb') as f:
                f.write(response.content)
            
            logger.info(f"{self.config.local_data_file} downloaded successfully!")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted zip file to: {unzip_path}")
        except zipfile.BadZipFile:
            raise zipfile.BadZipFile(f"The file at {self.config.local_data_file} is not a valid ZIP archive.")