import cv2
import os
import aiogram

def camera_image():
    current_dir = os.getcwd()
    cap = cv2.VideoCapture(0)
    for i in range(30):
        cap.read() 
    ret, frame = cap.read()
    cv2.imwrite(os.path.join(current_dir, 'dump', 'cam.png'), frame)
    cap.release()
