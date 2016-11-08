from unittest import TestCase
import cv2
import os
import numpy as np
import assess_composition.rule_of_thirds as thirds
from assess_composition.shot import Shot

class TestRuleOfThirds(TestCase):

    def test_check_overlapping(self):
        actual = thirds.check_overlap(333, (300, 350))
        self.assertEquals(actual, True)

    def test_check_not_overlapping(self):
        actual = thirds.check_overlap(333, (300, 330))
        self.assertEquals(actual, False)

    def test_draw_box(self):
        expected = Shot(np.zeros((1080,1920,1), np.uint8))
        boxes = np.array([[10, 10, 20, 20]])
        actual = thirds.draw_boxes(expected)
        cv2.rectangle(expected.frame, (10,10), (20,20), (127, 255, 0), 2)
        self.assertTrue((actual.frame==expected.frame).all())

    def test_draw_multiple_boxes(self):
        expected = Shot(np.zeros((1080,1920,1), np.uint8))
        boxes = np.array([[30, 30, 84, 72],[591, 832, 223, 580]])
        actual = thirds.draw_boxes(expected)
        cv2.rectangle(expected.frame, (30,30), (84,72), (127, 255, 0), 2)
        cv2.rectangle(expected.frame, (591,832), (223,580), (127, 255, 0), 2)
        self.assertTrue((actual.frame==expected.frame).all())

    def test_draw_lines(self):
        expected = Shot(np.zeros((1080,1920,1), np.uint8))
        actual = thirds.draw_lines(expected)
        cv2.line(expected.frame, (640, 0), (640, 1080), (0,0,255), 2)
        cv2.line(expected.frame, (1280, 0), (1280, 1080), (0,0,255), 2)
        cv2.line(expected.frame, (0, 360), (1920, 360), (0,0,255), 2)
        cv2.line(expected.frame, (0, 720), (1920, 720), (0,0,255), 2)
        self.assertTrue((actual.frame==expected.frame).all())

    def test_face_overlap_status(self):
        expected = "Face 1 overlaps vertical 2"
        img = cv2.imread('assess_composition/tests/imgs/facewidth2height1.png')
        shot = Shot(img)
        actual = thirds.report_overlap(shot)
        self.assertEqual(actual,expected)

    def test_face_no_overlap_status(self):
        expected = "Does not lie on thirds"
        img = cv2.imread('assess_composition/tests/imgs/facenothirds.png')
        shot = Shot(img)
        actual = thirds.report_overlap(shot)
        self.assertEqual(actual,expected)

    def test_face_vert_overlap_status(self):
        expected = "Face 1 overlaps vertical 1"
        img = cv2.imread('assess_composition/tests/imgs/facevert1.png')
        shot = Shot(img)
        actual = thirds.report_overlap(shot)
        self.assertEqual(actual,expected)

    def test_face_hor_overlap_status(self):
        expected = "Face 1 overlaps horizontal 1"
        img = cv2.imread('assess_composition/tests/imgs/facehor1.png')
        shot = Shot(img)
        actual = thirds.report_overlap(shot)
        self.assertEqual(actual,expected)

    def test_main(self):
        expected = thirds.main('assess_composition/tests/imgs/facewidth2height1.png')
        actual = cv2.imread('assess_composition/tests/imgs/testoutput.png')
        self.assertTrue((actual==expected).all())
