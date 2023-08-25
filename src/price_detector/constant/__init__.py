import os
from datetime import datetime
from dataclasses import dataclass


LOGS_DIR_NAME = "running_logs"
CURRENT_TIME_STAMP = datetime.strftime(datetime.now(),"%y-%m-%d-%H-%M-%S")
os.makedirs(name=LOGS_DIR_NAME,exist_ok=True)
LOG_FILE_PATH = os.path.join(LOGS_DIR_NAME,f"{CURRENT_TIME_STAMP}.log")

CONFIG_YAML_PATH = os.path.join("config","config.yaml")

@dataclass(frozen=True)
class ArtifactKey:
    ARTIFACT_ROOT_KEY:str = "artifact"
    ARTIFACT_ROOT_DIR_KEY:str = "root_dir"

@dataclass(frozen=True)
class DownloadModelKey:

    MODEL_ROOT_KEY :str = "load_pretrain_model"
    MODEL_ROOT_DIR_KEY :str = "root_dir"
    MODEL_DRIVE_ID_KEY :str = "model_id"
    MODEL_NAME_KEY :str = "model_name"


@dataclass(frozen=True)
class VegiDetectorKey:
    VEGI_DETECTOR_ROOT_KEY: str = "vegi_detector"
    VEGI_DETECTOR_ROOT_DIR_KEY: str = "root_dir"
    VEGI_DETECTOR_INPUT_FILE_NAME_KEY: str = "input_img_file_name"
    VEGI_DETECTOR_CROP_DIR_NAME_KEY: str = "crop_img_dir_name"

    


