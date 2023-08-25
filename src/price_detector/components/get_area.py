import cv2
import os
from price_detector.config import Configuration
from price_detector.entity import GetAreaConfig



class GetArea:
    def __init__(self):
        get_area_config = Configuration().get_area_config()
        self.canny_image_file_name  = get_area_config.canny_image_file_name
        self.erode_image_file_name  = get_area_config.erode_image_file_name
        self.dillate_image_file_name  = get_area_config.dillate_image_file_name
        self.crop_images_dir_name = get_area_config.crop_images_dir_name

    def preprocessing(self):

        for img_path in os.listdir(self.crop_images_dir_name):
            img=cv2.imread(img_path)
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            blur_img=cv2.GaussianBlur(gray_img,(7,7),1)
            canny_img=cv2.Canny(blur_img,40,40)
            kernel=np.ones((5,5))
            dilate_img=cv2.dilate(canny_img,kernel,iterations=3)
            erode_img=cv2.erode(dilate_img,kernel,iterations=2)
            return erode_img,img
