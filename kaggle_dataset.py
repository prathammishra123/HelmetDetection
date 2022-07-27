import pandas as pd
import numpy as np
import shutil

df = pd.read_csv("./labels/labels.csv", sep=",")
df = df.drop(["xmin", "ymin", "xmax", "ymax", "width", "height"], axis=1)
df = df.drop_duplicates(subset="filename", keep="first")

for idx, row in df.iterrows():
    src = f"./labels/images/{row['filename']}"
    dst = f"./Dataset/{row['class'].replace(' ', '')}/{row['filename']}"
    shutil.copy(src, dst)