import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import os
import cv2

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

model = keras.Sequential([
    keras.layers.Conv2D(100, (3, 3), input_shape=(100, 100, 1), activation="relu"),
    keras.layers.Conv2D(200, (3, 3), activation="relu"),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(100, (3, 3), activation="relu"),
    keras.layers.Conv2D(200, (3, 3), activation="relu"),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dropout(0.4),
    keras.layers.Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(train_image, train_label, epochs=10)
print(model.evaluate(test_image, test_label))

model.save("./model.h5")