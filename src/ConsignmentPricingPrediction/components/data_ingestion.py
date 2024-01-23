from ConsignmentPricingPrediction.entity import DataIngestionConfig
from ConsignmentPricingPrediction.logging import Logger
import urllib.request as request
import os
import zipfile

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.config = data_ingestion_config

    def download_file(self):
        if os.path.exists(self.config.local_data_file):
            Logger.info(f"{self.config.local_data_file} already exists")
        else:
            filename, header = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            Logger.info(f"File Downloaded:{filename} | \nHeaders: {header}")

    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
    
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

        Logger.info(f"{unzip_path} extracted")

    def initiate_data_ingestion(self):
        self.download_file()
        self.extract_zip_file()
