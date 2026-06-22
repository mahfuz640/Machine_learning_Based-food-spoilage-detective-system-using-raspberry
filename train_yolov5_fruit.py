import os
import random
import shutil
from pathlib import Path

# ============================================
# DATASET PATH
# ============================================
DATASET_PATH = "App"

# ============================================
# YOLO DATASET PATH
# ============================================
YOLO_PATH = "dataset"

# ============================================
# CLASSES
# ============================================
classes = {
    "AppleFresh": 0,
    "AppleSpoiled": 1,
    "BananaFresh": 2,
    "BananaSpoiled": 3
}

# ============================================
# CREATE FOLDERS
# ============================================
folders = [
    "images/train",
    "images/val",
    "labels/train",
    "labels/val"
]

for folder in folders:
    os.makedirs(os.path.join(YOLO_PATH, folder), exist_ok=True)

# ============================================
# PROCESS IMAGES
# ============================================
for class_name, class_id in classes.items():

    class_folder = os.path.join(DATASET_PATH, class_name)

    images = os.listdir(class_folder)

    random.shuffle(images)

    split = int(len(images) * 0.8)

    train_images = images[:split]
    val_images = images[split:]

    for mode, image_list in [("train", train_images), ("val", val_images)]:

        for img_name in image_list:

            src = os.path.join(class_folder, img_name)

            dst = os.path.join(
                YOLO_PATH,
                f"images/{mode}",
                f"{class_name}_{img_name}"
            )

            shutil.copy(src, dst)

            label_name = Path(dst).stem + ".txt"

            label_path = os.path.join(
                YOLO_PATH,
                f"labels/{mode}",
                label_name
            )

            # FULL IMAGE OBJECT
            with open(label_path, "w") as f:
                f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")

print("Dataset Ready")

# ============================================
# CREATE YAML
# ============================================
yaml_text = f"""
path: {os.path.abspath(YOLO_PATH)}

train: images/train
val: images/val

names:
  0: AppleFresh
  1: AppleSpoiled
  2: BananaFresh
  3: BananaSpoiled
"""

with open("fruit.yaml", "w") as f:
    f.write(yaml_text)

print("fruit.yaml Created")

# ============================================
# TRAIN YOLOv8
# ============================================
from ultralytics import YOLO

model = YOLO("yolov8m.pt")

model.train(
    data="fruit.yaml",
    epochs=100,
    imgsz=640,
    batch=8
)

print("Training Complete")