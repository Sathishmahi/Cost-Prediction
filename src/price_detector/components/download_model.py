from price_detector.config import Configuration
from price_detector import logging
import gdown



def download_model(configuration:Configuration = Configuration() )->None:

    model_id = configuration.get_download_model_config().model_id
    model_name = configuration.get_download_model_config().model_name

    gdown.download(id = model_id,output = model_name )


if __name__ == "__main__":
    download_model()