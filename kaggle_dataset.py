import pandas as pd
import numpy as np
import shutil
# This file puts kaggle dataset in with and without helmet without appyling face cascades and augmentation
# Rem-kaggle dataset is present in labels folder inside images it contains labbelled images and csv file has information related to these images
df = pd.read_csv("./labels/labels.csv", sep=",")
df = df.drop(["xmin", "ymin", "xmax", "ymax", "width", "height"], axis=1)
df = df.drop_duplicates(subset="filename", keep="first")
# Here we copy the images from kaggle dataset in to initial dataset
for idx, row in df.iterrows():
    src = f"./labels/images/{row['filename']}"
    dst = f"./Dataset/{row['class'].replace(' ', '')}/{row['filename']}"
    shutil.copy(src, dst)