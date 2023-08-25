import os
import shutil
import yaml
from price_detector import logging
from price_detector.constant import CONFIG_YAML_PATH
from pathlib import Path


def read_yaml(yaml_path:str | Path = CONFIG_YAML_PATH)->dict:
    if not os.path.exists(yaml_path):
        e = f" yaml file not found {yaml_path} "
        raise FileNotFoundError(e)
    with open(yaml_path,mode="r") as yf:
        content = yaml.safe_load(yf)
    return content

def make_dirs(dir_list:list[Path],exist_ok:bool=True)->None:
    try:
        for dir in dir_list:
            if exist_ok:
                os.makedirs(dir,exist_ok=exist_ok)
            else:
                if os.path.isfile(dir):
                    raise NotADirectoryError(f" dir must be floder not a file {dir} ")
                shutil.rmtree(dir) 
                os.makedirs(dir)
            logging.info(msg=f"folder created {dir}")

    except Exception as e:
        logging.exception(msg=f" error occured {e}  ")
        raise e