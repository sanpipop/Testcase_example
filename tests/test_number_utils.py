from test_6610110661.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_5_7_11_is_prime(self):
        prime_list = [5, 7, 11]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_13_17_19_is_prime(self):
        prime_list = [13, 17, 19]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_23_29_31_is_prime(self):
        prime_list = [23, 29, 31]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_37_41_43_is_prime(self):
        prime_list = [37, 41, 43]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_47_53_59_is_prime(self):
        prime_list = [47, 53, 59]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    