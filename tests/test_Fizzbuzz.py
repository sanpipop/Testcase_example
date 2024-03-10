from test_6610110661.Fizzbuzz import fizzbuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_6_9(self):
        lst_num = [3, 6, 9]
        for num in lst_num:
            self.assertEqual(fizzbuzz(num), 'Fizz')

    def test_give_5_10_20(self):
        lst_num = [5, 10, 20]
        for num in lst_num:
            self.assertEqual(fizzbuzz(num), 'Buzz')

    def test_give_15_30_45(self):
        lst_num = [15, 30, 45]
        for num in lst_num:
            self.assertEqual(fizzbuzz(num), 'FizzBuzz')

    def test_give_0(self):
        self.assertEqual(fizzbuzz(0), 'FizzBuzz')

    def test_give_negative_numbers(self):
        lst_num = [-3, -6, -9]
        for num in lst_num:
            self.assertEqual(fizzbuzz(num), 'Fizz')

