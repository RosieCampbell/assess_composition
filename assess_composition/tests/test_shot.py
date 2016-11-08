from unittest import TestCase
import cv2
import numpy as np
from assess_composition.shot import Shot

class TestShot(TestCase):

    def test_create_shot(self):
        img = cv2.imread('assess_composition/tests/imgs/facewidth2height1.png')
        actual = Shot(img).frame
        self.assertTrue((actual==img).all())

    def test_get_width(self):
        img = np.zeros((1080,1920,1), np.uint8)
        actual = Shot(img).width
        self.assertEquals(actual, 1920)

    def test_get_height(self):
        img = np.zeros((1080,1920,1), np.uint8)
        actual = Shot(img).height
        self.assertEquals(actual, 1080)

    def test_get_first_horizontal_third_line(self):
        img = np.zeros((1080,1920,1), np.uint8)
        actual = Shot(img).horizontal_thirds()[0]
        self.assertEquals(actual,((0, 360),(1920, 360)))

    def test_get_second_horizontal_third_line(self):
        img = np.zeros((1080,1920,1), np.uint8)
        actual = Shot(img).horizontal_thirds()[1]
        self.assertEquals(actual,((0, 720),(1920, 720)))

    def test_get_first_vertical_third_line(self):
        img = np.zeros((1080,1920,1), np.uint8)
        actual = Shot(img).vertical_thirds()[0]
        self.assertEquals(actual, ((640,0),(640, 1080)))

    def test_get_second_vertical_third_line(self):
        img = np.zeros((1080,1920,1), np.uint8)
        actual = Shot(img).vertical_thirds()[1]
        self.assertEquals(actual, ((1280,0),(1280, 1080)))

    def test_get_first_vertical_third_value(self):
        img = np.zeros((1080,1920,1), np.uint8)
        actual = Shot(img).get_third("h", 0)
        self.assertEqual(actual, 360)

    def test_get_first_horizontal_third_value(self):
        img = np.zeros((1080,1920,1), np.uint8)
        actual = Shot(img).get_third("v", 0)
        self.assertEqual(actual, 640)

    def test_detect_faces(self):
        img = cv2.imread('assess_composition/tests/imgs/facewidth2height1.png')
        actual = Shot(img).get_faces()[0]
        expected = np.array([1201, 152, 1442, 393])
        self.assertTrue((actual==expected).all())
