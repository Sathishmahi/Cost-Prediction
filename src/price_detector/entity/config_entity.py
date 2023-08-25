from collections import namedtuple


GetAreaConfig = namedtuple("GetAreaConfig", [
    
    "root_dir",
    "canny_image_file_name",
    "dillate_image_file_name",
    "erode_image_file_name",
    "crop_images_dir_name"

]
    
)

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