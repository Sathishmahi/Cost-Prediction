from collections import namedtuple


DownloadModelConfig = namedtuple("DownloadModelConfig", 
                        [
                            "root_dir",
                            "model_id",
                            "model_name"
                        ]
                        )



VegiDetectorConfig = namedtuple("VegiDetectorConfig",
                     [
                        "root_dir",
                        "input_img_file_name",
                        "crop_img_dir_name",
                        "model_path"
                     ]
                     )