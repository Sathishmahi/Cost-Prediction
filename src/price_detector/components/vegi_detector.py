from price_detector.config import Configuration
from price_detector.entity import VegiDetectorConfig
from ultralytics import YOLO
import os
import cv2



class VegiDetect:
    def __init__(self,configuration = Configuration()):
        self.vegi_detector_config = configuration.get_vegi_detector_config()
        self.crop_img_dir_name = self.vegi_detector_config.crop_img_dir_name
        self.input_img_file_name = self.vegi_detector_config.input_img_file_name
        self.model_path = self.vegi_detector_config.model_path

    @staticmethod
    def load_model(model_path)->YOLO:
        return YOLO(model = model_path)
    
    def detect(self):
        model = self.load_model(self.model_path)
        self.classes = model.names
        result = model.predict(self.input_img_file_name)
        return result

    def crop_imgs(self):
        result = self.detect()
        bboxes = result[0].boxes.boxes
        imarr = cv2.imread(self.input_img_file_name)
        for id,box in enumerate(bboxes,start=1):
            x1,y1,x2,y2,cof,cl = box
            img_path =  os.path.join(self.crop_img_dir_name,f"frame_1_{id}_{self.classes[cl.item()]}.jpg")
            cv2.imwrite(img_path,imarr[int(y1):int(y2),int(x1):int(x2)])


        

if __name__ == "__main__":
    vegi_detector= VegiDetect()
    vegi_detector.crop_imgs()