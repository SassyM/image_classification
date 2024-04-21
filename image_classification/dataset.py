from torch.utils.data import Dataset
import os
from PIL import Image
import glob

class DeforestationDataset(Dataset):

    def __init__(self, img_dir, transform=None):
        self.img_paths = glob.glob(os.path.join(img_dir, r"*\*.png"))
        self.classes = os.listdir(img_dir)
        self.transform = transform

    def __len__(self):
        return len(self.img_paths)

    def __getitem__(self, idx):
        path = self.img_paths[idx]
        image = Image.open(path)
        label = path.split("\\")[-2]
        
        if self.transform:
            return self.transform(image), label
        else:
            return image, label 