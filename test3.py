import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "faces")

labels = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        print(root[root.rfind('/') + 1:])