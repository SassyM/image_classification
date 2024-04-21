# from torch.utils.data import DataLoader
from dataset import DeforestationDataset
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
import glob

# train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
# test_loader = DataLoader(test_dataset, batch_size=64, shuffle=True)

# lanscape_dataset = DeforestationDataset(r"C:\Users\srish\Hackathon\train.csv", r"C:\Users\srish\Hackathon\train_test_data")

fig = plt.figure()  

# for i, sample in enumerate(lanscape_dataset):
#     print(i, sample['image'].shape, sample['landmarks'].shape)

#     ax = plt.subplot(1, 4, i + 1)
#     plt.tight_layout()
#     ax.set_title('Sample #{}'.format(i))
#     ax.axis('off')
#     lanscape_dataset(**sample)

#     if i == 3:
#         plt.show()
#         break
img_dir = r"C:\Users\srish\Hackathon\train_test_data\train\0"
images = os.listdir(img_dir)
for path in images[:1]:
    img_path = os.path.join(img_dir, path)
    image = Image.open(img_path)
    image = np.array(image)
    print(image.shape)
    plt.imshow(image)
    plt.show()
