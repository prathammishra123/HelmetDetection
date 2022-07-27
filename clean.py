# TODO: Use haarcascade to get faces (codebasics playlist)
# TODO: Reduce to same size
# TODO: Turn to grayscale
# TODO: Save in new folder
import numpy as np
import cv2
# from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

# function to get clear face of an image which returns a cropped image of a face if face is detected properly.
def get_cropped_image_if_2_eyes(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        try:
            roi_gray = gray[y-30:y+h+50, x-30:x+w+30]
            roi_color = img[y-30:y+h+50, x-30:x+w+30]
            # eyes = eye_cascade.detectMultiScale(roi_gray)
            # if len(eyes) >= 2:
            # print(type(roi_color))
            roi_color_resize=cv2.resize(roi_color, (100,100))
            return roi_color_resize
        except Exception as e:
            continue
    return None


# store path in a variable 
path_to_data = "./dataset/"
path_to_cr_data = "./dataset/cropped/"

# for storing withelmet and withouthelmet path in img_dirs 
import os
img_dirs = []
for entry in os.scandir(path_to_data):
    if entry.is_dir():
        img_dirs.append(entry.path)

# to make a new folder named cropped in dataset folder 
#  first check if it exist then remove it and then make cropped folder in dataset 
import shutil
if os.path.exists(path_to_cr_data):
     shutil.rmtree(path_to_cr_data)
os.mkdir(path_to_cr_data)

# this function iterates all images and if the image is proper it stores  that inside cropped folder inside folder of withHelmet or WithoutHelmet whichever it belongs to
cropped_image_dirs = []
celebrity_file_names_dict = {}

for img_dir in img_dirs:
    count = 1
    celebrity_name = img_dir.split('/')[-1]
    print(celebrity_name)
    
    celebrity_file_names_dict[celebrity_name] = []
    
    for entry in os.scandir(img_dir):
        roi_color = get_cropped_image_if_2_eyes(entry.path)
        
        if roi_color is not None:
            cropped_folder = path_to_cr_data + celebrity_name
            if not os.path.exists(cropped_folder):
                os.makedirs(cropped_folder)
                cropped_image_dirs.append(cropped_folder)
                print("Generating cropped images in folder: ",cropped_folder)
                
            cropped_file_name = celebrity_name + str(count) + ".png"
            cropped_file_path = cropped_folder + "/" + cropped_file_name 
            print(cropped_file_path)
            cv2.imwrite(cropped_file_path, roi_color)
            celebrity_file_names_dict[celebrity_name].append(cropped_file_path)
            count += 1 