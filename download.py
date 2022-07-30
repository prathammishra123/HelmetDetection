import requests
import cv2
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
import time

model = keras.models.load_model("./model.h5")

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

classes = {0: "No helmet", 1: "Helmet found"}

def get_cropped_image_if_2_eyes(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        try:
            roi_gray = gray[y-30:y+h+50, x-30:x+w+30]
            roi_color = img[y-30:y+h+50, x-30:x+w+30]
            roi_color_resize=cv2.resize(roi_gray, (100,100))
            return roi_color_resize
        except Exception as e:
            return cv2.resize(gray, (100, 100))

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def find_faults(url):
    # url = "https://drive.google.com/file/d/11q7_j10LGkg0QOlTNur5yl2zIB7x_mV_/view?usp=sharing"
    file_id = url.split("/")[-2]
    destination = './input.mp4'
    download_file_from_google_drive(file_id, destination)

    cap = cv2.VideoCapture(destination)

    if not cap.isOpened():
        print("Error opening video file")

    results = []

    start_time = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            frame_img = get_cropped_image_if_2_eyes(frame)
            if frame_img is not None:
                end_time = time.time()
                cv2.imshow('Frame', frame_img)
                if end_time - start_time < 5:
                    continue
                prediction = model.predict(frame_img.reshape(1,100,100,1),batch_size = 1)
                if int(prediction[0][0]) == 0:
                    results.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                start_time = time.time()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    os.remove(destination)
    return results
