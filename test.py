import sys
sys.path.append("..")
from segment_anything import sam_model_registry, SamPredictor

sam_checkpoint = "src/price_detector/notebooks/sam_vit_h_4b8939.pth"
model_type = "vit_h"

device = "cpu"



sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)