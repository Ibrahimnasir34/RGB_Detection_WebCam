import numpy as np
import cv2
from PIL import Image

def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
    upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

# Define colors to detect (BGR format)
colors = {
    "Yellow": [0, 255, 255],
    "Red": [0, 0, 255],
    "Green": [0, 255, 0],
    "Blue": [255, 0, 0]
}

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream or file")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, color_value in colors.items():
        lowerLimit, upperLimit = get_limits(color=color_value)
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, color_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
