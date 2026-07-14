import numpy as np
import pandas as pd
import torch 
import random

def set_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)

def get_torch_device():
    if torch.cuda.is_available():
        return torch.device("cuda")
    else:
        return torch.device("cpu")

def get_img_files(dataset_path):
    image_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img.path).convert("RGB")
            img_array = np.array(img)
            image_data.append(img_array)
        image_data = np.array(image_data)
    return image_data
