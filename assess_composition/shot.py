import cv2
import numpy as np

class Shot:

    def __init__(self, frame):
        self.frame = frame
        self.width = self.frame.shape[1]
        self.height = self.frame.shape[0]

    def horizontal_thirds(self):
        first_horizontal_third = ((0, self.height/3),(self.width, self.height/3))
        second_horizontal_third = ((0,2*self.height/3),(self.width,2*self.height/3))
        return (first_horizontal_third,second_horizontal_third)

    def vertical_thirds(self):
        first_vertical_third = ((self.width/3,0),(self.width/3,self.height))
        second_vertical_third = ((2*self.width/3,0),(2*self.width/3,self.height))
        return (first_vertical_third,second_vertical_third)

    def get_faces(self):
        cascade = cv2.CascadeClassifier("/usr/local/Cellar/opencv/2.4.13.1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml")
        rects = cascade.detectMultiScale(self.frame, 1.1, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (10,10))
        if len(rects) == 0:
            return []
        rects[:, 2:] += rects[:, :2]
        return rects
