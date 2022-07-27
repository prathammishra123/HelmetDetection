import tensorflow as tf
import numpy as np
import cv2
import os

augmented_with = []
for img_path in os.listdir("./Dataset/cropped/WithHelmet"):
    img = cv2.imread(f"./Dataset/cropped/WithHelmet/{img_path}")
    img_hflip = np.array(tf.image.flip_left_right(img))
    img_vflip = np.array(tf.image.flip_up_down(img))
    img_brt = np.array(tf.image.random_brightness(img, 0.2))
    augmented_with.append(img)
    augmented_with.append(img_hflip)
    augmented_with.append(img_vflip)
    augmented_with.append(img_brt)

for idx, img in enumerate(augmented_with):
    cv2.imwrite(f"./Dataset/cropped/Augmented/WithHelmet/WithHelmet{idx + 1}.png", img)

augmented_without = []
for img_path in os.listdir("./Dataset/cropped/WithoutHelmet"):
    img = cv2.imread(f"./Dataset/cropped/WithoutHelmet/{img_path}")
    img_hflip = np.array(tf.image.flip_left_right(img))
    img_vflip = np.array(tf.image.flip_up_down(img))
    img_brt = np.array(tf.image.random_brightness(img, 0.2))
    augmented_without.append(img)
    augmented_without.append(img_hflip)
    augmented_without.append(img_vflip)
    augmented_without.append(img_brt)

for idx, img in enumerate(augmented_without):
    cv2.imwrite(f"./Dataset/cropped/Augmented/WithoutHelmet/WithoutHelmet{idx + 1}.png", img)