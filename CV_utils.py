import numpy as np
import cv2
from controller import Robot
from controller import Camera
from vehicle import Car
import matplotlib.pyplot as plt
from controller import Display

def get_image(camera):
    base_image = camera.getImage()
    image = np.frombuffer(base_image, np.uint8)
    image = image.reshape(camera.getHeight(), camera.getWidth(), 4)
    return image

def convert_binary_image (image, colour, error):
    hsv= cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_border= colour - error/2
    higher_border = colour + error/2
    mask = cv2.inRange(hsv, lower_border, higher_border)
    return mask

def calculate_average_col_and_norm_col (binary_image):
    th_idx = np.where(binary_image =255)
    if  not th_idx:
        print("Warning: In Binary image all pixels are zero")
        return None, None
    else:
        average_column = np.average(th_idx[1])
        norm_column = (average_column - binary_image.sahape[1]/2)/ binary_image.shape[1]
        return norm_column, average_column

def display_binary_image (display_th, binary_image, average_column):
    binary_image_rgba = np.dstack((binary_image, binary_image, binary_image))
    binary_image_rgba[:, average_column, 0] = 255
    binary_image_rgba[:, average_column, 1] = 0
    binary_image_rgba[:, average_column, 2] = 0
    image_ref = display_th.immageNew(binary_image_rgba.tobytes(), 
                                     Display.RGB, 
                                     width = binary_image_rgba.shape[1],
                                     height=binary_image_rgba.shape[0])
    display_th.imagePaste(image_ref,0,0, False)


