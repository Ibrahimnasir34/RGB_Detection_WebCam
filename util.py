import numpy as np
import cv2


def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = hsvC[0][0][0]  # Get the hue value
    lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
    upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    return lowerLimit, upperLimit
