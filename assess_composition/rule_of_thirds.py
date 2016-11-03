import cv2
import numpy as np
import os
from assess_composition.shot import Shot

def calculate_thirds(num):
    return (num/3, 2*num/3)

def check_overlap(third_line, rect_Line):
    return third_line > rect_Line[0] and third_line < rect_Line[1]

def draw_lines(shot):
    for line in shot.vertical_thirds():
        cv2.line(shot.frame, line[0], line[1], (0,0,255), 2)
    for line in shot.horizontal_thirds():
        cv2.line(shot.frame, line[0], line[1], (0,0,255), 2)
    return shot

def draw_boxes(shot):
    for box in shot.get_faces():
        cv2.rectangle(shot.frame, (box[0], box[1]), (box[2], box[3]), (127, 255, 0), 2)
    return shot

def main(path):
    img = cv2.imread(path)
    shot = Shot(img)
    draw_boxes(shot)
    draw_lines(shot)
    cv2.imwrite('out.png', shot.frame)
    return img


if __name__ == "__main__":
    main()
