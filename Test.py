import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import os
import cv2
from sklearn.model_selection import train_test_split
#  Here I load the model
model = keras.models.load_model("./model.h5")
#  This is path to the final dataset ie data after being augmented
PATH = "./Dataset/cropped/Augmented"

images = []
labels = []

for label in os.listdir(PATH):
    CUR_PATH = f"{PATH}/{label}"
    for img_name in os.listdir(CUR_PATH):
        img_path = f"{CUR_PATH}/{img_name}"
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img = cv2.resize(img,(100, 100))
        img = np.array(img)
        img = img.astype("float32")
        img /= 255
        images.append(img)
        labels.append(1 if label[:-6] == "With" else 0)

images = np.array(images)
labels = np.array(labels)
images = images.reshape(-1,100,100,1)
train_image, test_image, train_label, test_label = train_test_split(images,labels,shuffle=True,test_size = 0.1)
print("Test non helmet",np.count_nonzero(test_label==0))
print("Test with helmet",np.count_nonzero(test_label==1))
print("Train non helmet",np.count_nonzero(train_label==0))
print("Train with helmet",np.count_nonzero(train_label==1))
print(model.evaluate(test_image, test_label))