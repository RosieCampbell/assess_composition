from unittest import TestCase
import cv2
import os
import numpy as np
import assess_composition.rule_of_thirds as thirds

class TestRuleOfThirds(TestCase):
    def test_get_width(self):
        img = cv2.imread('assess_composition/tests/imgs/test.png')
        actual = thirds.width(img)
        self.assertEquals(actual, 1920)

    def test_get_height(self):
        img = cv2.imread('assess_composition/tests/imgs/test.png')
        actual = thirds.height(img)
        self.assertEquals(actual, 1080)

    def test_calculate_thirds(self):
        actual = thirds.calculate_thirds(999)
        self.assertEquals(actual, (333, 666))

    def test_check_overlapping(self):
        actual = thirds.check_overlap(333, (300, 350))
        self.assertEquals(actual, True)

    def test_check_not_overlapping(self):
        actual = thirds.check_overlap(333, (300, 330))
        self.assertEquals(actual, False)

    def test_get_one_face(self):
        img = cv2.imread('assess_composition/tests/imgs/test.png')
        actual = thirds.get_faces(img)[0]
        expected = np.array([1201, 152, 1442, 393])
        self.assertEquals((actual==expected).all(), True)

    def test_draw_box(self):
        expected = np.zeros((1080,1920,1), np.uint8)
        boxes = np.array([[10, 10, 20, 20]])
        actual = thirds.draw_boxes(expected, boxes)
        cv2.rectangle(expected, (10,10), (20,20), (127, 255, 0), 2)
        self.assertEquals((actual==expected).all(), True)

    def test_draw_multiple_boxes(self):
        expected = np.zeros((1080,1920,1), np.uint8)
        boxes = np.array([[30, 30, 84, 72],[591, 832, 223, 580]])
        actual = thirds.draw_boxes(expected, boxes)
        cv2.rectangle(expected, (30,30), (84,72), (127, 255, 0), 2)
        cv2.rectangle(expected, (591,832), (223,580), (127, 255, 0), 2)
        self.assertEquals((actual==expected).all(), True)

    def test_draw_lines(self):
        expected = np.zeros((1080,1920,1), np.uint8)
        actual = thirds.draw_lines(expected)
        cv2.line(expected, (640, 0), (640, 1080), (0,0,255), 2)
        cv2.line(expected, (1280, 0), (1280, 1080), (0,0,255), 2)
        cv2.line(expected, (0, 360), (1920, 360), (0,0,255), 2)
        cv2.line(expected, (0, 720), (1920, 720), (0,0,255), 2)
        self.assertEquals((actual==expected).all(), True)

    def test_main(self):
        expected = thirds.main('assess_composition/tests/imgs/test.png')
        actual = cv2.imread('assess_composition/tests/imgs/testoutput.png')
        self.assertEquals((actual==expected).all(), True)
