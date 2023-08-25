import os
from price_detector.entity import DownloadModelConfig,VegiDetectorConfig
from price_detector.utils import read_yaml,make_dirs
from price_detector.constant import DownloadModelKey,ArtifactKey,VegiDetectorKey


class Configuration:
    def __init__(self):
        self.config_content = read_yaml()
        artifact_content = self.config_content.get(ArtifactKey.ARTIFACT_ROOT_KEY)
        self.artifact_root_dir = artifact_content.get(ArtifactKey.ARTIFACT_ROOT_DIR_KEY)
        make_dirs([self.artifact_root_dir])




    def get_vegi_detector_config(self)->VegiDetectorConfig:

        vegit_detector_content  = self.config_content.get(VegiDetectorKey.VEGI_DETECTOR_ROOT_KEY)
        root_dir  = os.path.join(self.artifact_root_dir,vegit_detector_content.get(VegiDetectorKey.VEGI_DETECTOR_ROOT_DIR_KEY))
        input_img_file_name = os.path.join(root_dir,vegit_detector_content.get(VegiDetectorKey.VEGI_DETECTOR_INPUT_FILE_NAME_KEY))
        crop_img_dir_name = os.path.join(root_dir,vegit_detector_content.get(VegiDetectorKey.VEGI_DETECTOR_CROP_DIR_NAME_KEY))
        model_path =  self.get_download_model_config().model_name
        make_dirs([root_dir,crop_img_dir_name])
        return VegiDetectorConfig(root_dir, input_img_file_name, crop_img_dir_name,model_path)
    
    def get_download_model_config(self)->DownloadModelConfig:

        download_model_config = self.config_content.get(DownloadModelKey.MODEL_ROOT_KEY)
        
        root_dir = os.path.join(self.artifact_root_dir,download_model_config.get(DownloadModelKey.MODEL_ROOT_DIR_KEY))

        model_id = download_model_config.get(DownloadModelKey.MODEL_DRIVE_ID_KEY)

        model_name = os.path.join(root_dir,download_model_config.get(DownloadModelKey.MODEL_NAME_KEY))

        make_dirs([root_dir])

        return DownloadModelConfig(root_dir, model_id, model_name)
