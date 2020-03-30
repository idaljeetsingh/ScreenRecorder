"""
    Title: ScreenRecorder
    Module Name: record_screen
    Author: Daljeet Singh Chhabra
    Language: Python
    Date Created: 30-03-2020
    Date Modified: 30-03-2020
"""
from PIL import ImageGrab
import numpy as np
import cv2


def start_record(savefilename):
    fourcc = cv2.VideoWriter_fourcc(*'xvid')

    out = cv2.VideoWriter(savefilename + '.avi', fourcc, 15, (1920, 1080))
    while True:
        img = ImageGrab.grab()
        img_BGR = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(img_BGR)
        cv2.imshow("ScreenCapture", cv2.resize(img_BGR, (160, 90)))
        key = cv2.waitKey(1)
        if key == 27:           # Pressing ESC will stop recording.
            out.release()
            break

    cv2.destroyAllWindows()


filename = input('Enter new recording name: ')
start_record(filename)
