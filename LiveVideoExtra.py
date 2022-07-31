# This is a extra file through which I can open my live camera and apply my model 
import cv2
import tensorflow as tf
from tensorflow import keras
# loading model
model = keras.models.load_model("./model.h5")
# importing face and eyes cascades
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

classes = {0: "No helmet", 1: "Helmet found"}
#  functionn to detect face
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
# starting live video here 
vid = cv2.VideoCapture(0)
while (True) :
    ret, frame = vid.read()
    frame_img = get_cropped_image_if_2_eyes(frame)
    if frame_img is not None:
        cv2.imshow("frame", frame_img)
        prediction = model.predict(frame_img.reshape(1,100,100,1),batch_size = 1)
        # print(classes[prediction[0].argmax()])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()