from test_6610110661.cat_and_mouse import cat_and_mouse
import unittest

class CatAndMouseTest(unittest.TestCase):
    def test_catA1_catB2_mouseC3(self):
        result = cat_and_mouse(1, 2, 3)
        self.assertEqual(result, "Cat B")
    def test_catA1_catB3_mouseC2(self):
        result = cat_and_mouse(1, 3, 2)
        self.assertEqual(result, "Mouse C")
    def test_catA1_catB5_mouseC4(self):
        result = cat_and_mouse(1, 5, 4)
        self.assertEqual(result, "Cat B")
    def test_catA5_catB4_mouseC2(self):
        result = cat_and_mouse(5, 4, 2)
        self.assertEqual(result, "Cat B")
    def test_catA6_catB7_mouseC5(self):
        result = cat_and_mouse(6, 7, 5)
        self.assertEqual(result, "Cat A")
    def test_catA7_catB8_mouseC9(self):
        result = cat_and_mouse(7, 8, 9)
        self.assertEqual(result, "Cat B")
    def test_catA8_catB9_mouseC10(self):
        result = cat_and_mouse(8, 9, 10)
        self.assertEqual(result, "Cat B")
    def test_catAminus1_catB9_mouseCminus10(self):
        result = cat_and_mouse(-1, 9, -10)
        self.assertEqual(result, "Cat A")
    def test_catAminus8_catBminus9_mouseC10(self):
        result = cat_and_mouse(-8, -9, 10)
        self.assertEqual(result, "Cat A")
    def test_catA1_catB1_mouseC1(self):
        result = cat_and_mouse(1, 1, 1)
        self.assertEqual(result, "Mouse C")
    def test_catA1_catB1_mouseC10(self):
        result = cat_and_mouse(1, 1, 10)
        self.assertEqual(result, "Mouse C")
    def test_catA1_catB10_mouseC10(self):
        result = cat_and_mouse(1, 10, 10)
        self.assertEqual(result, "Cat B")


