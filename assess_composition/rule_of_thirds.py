import cv2
import numpy as np
import os

def calculate_thirds(num):
    return (num/3, 2*num/3)

def check_overlap(third_line, rect_Line):
    return third_line > rect_Line[0] and third_line < rect_Line[1]

def get_faces(img):
    cascade = cv2.CascadeClassifier("/usr/local/Cellar/opencv/2.4.13.1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml")
    rects = cascade.detectMultiScale(img, 1.1, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (10,10))
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects

def width(img):
    return img.shape[1]

def height(img):
    return img.shape[0]

def calculate_width_line(img, a):
    line = ((a, 0),(a, height(img)))
    cv2.line(img, line[0], line[1], (0,0,255), 2)
    return line

def calculate_height_line(img, a):
    line = ((0, a),(width(img), a))
    cv2.line(img, line[0], line[1], (0,0,255), 2)
    return line

def draw_lines(img):
    widthLine1 = calculate_width_line(img, (calculate_thirds(width(img))[0]))
    widthLine2 = calculate_width_line(img, (calculate_thirds(width(img))[1]))
    heightLine1 = calculate_height_line(img, calculate_thirds(height(img))[0])
    heightLine2 = calculate_height_line(img, calculate_thirds(height(img))[1])
    return img

def draw_boxes(img, boxes):
    for box in boxes:
        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (127, 255, 0), 2)
    return img

def main(path):
    img = cv2.imread(path)
    faces = get_faces(img)
    widthThirds = calculate_thirds(width(img))
    heightThirds = calculate_thirds(height(img))
    for face in faces:
        if check_overlap(widthThirds[0], (face[0], face[2])):
            print "Face lies on first width third"
        if check_overlap(widthThirds[1], (face[0], face[2])):
            print "Face lies on second width third"
        if check_overlap(heightThirds[0], (face[1], face[3])):
            print "Face lies on first height third"
        if check_overlap(heightThirds[1], (face[1], face[3])):
            print "Face lies on second height third"
    draw_boxes(img, faces)
    draw_lines(img)
    cv2.imwrite('out.png', img)
    return img


if __name__ == "__main__":
    main()
