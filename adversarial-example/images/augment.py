import os, cv2, random, glob
from albumentations import (
    Compose, HorizontalFlip, VerticalFlip,
    RandomRotate90, Transpose, RandomCrop,
    OneOf, HueSaturationValue, GaussNoise
)
from tqdm import tqdm

seed_dir = "raw"
images   = [cv2.imread(p) for p in glob.glob(os.path.join(seed_dir, "*.png"))]

transform = Compose([
    OneOf([HorizontalFlip(p=0.5), VerticalFlip(p=0.5)]),
    RandomRotate90(),
    Transpose(p=0.2),
    RandomCrop(height=128, width=128, p=1.0),
    HueSaturationValue(p=0.3),
    GaussNoise(var_limit=(10, 50), p=0.2)
], p=1.0)

aug_dir = "aug"
os.makedirs(aug_dir, exist_ok=True)

num_per_seed = 50

for idx, img in enumerate(tqdm(images)):
    for i in range(num_per_seed):
        aug = transform(image=img)["image"]
        fname = f"key_{idx}_{i:03d}.png"
        cv2.imwrite(os.path.join(aug_dir, fname), aug)

