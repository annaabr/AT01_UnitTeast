import unittest

from main import add, subtract, multiply, divide, is_even, remainder

# ---------------------------------------------------------
# Домашнее задание
class TestRemainder(unittest.TestCase):
    def test_remainder_success(self):
        self.assertEqual(remainder(10, 2), 0)
        self.assertEqual(remainder(-6, 4), 2)
        self.assertEqual(remainder(5, 2), 1)
        self.assertEqual(remainder(6, -4), -2)
        self.assertEqual(remainder(5, -2), -1)

    def test_remainder_by_zero(self):
        self.assertRaises(ValueError, remainder, 6, 0)
        self.assertRaises(TypeError, remainder, 6, 'a')
# ---------------------------------------------------------

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    # def test_divide(self):
    #    self.assertNotEqual(divide(4, 2), 3)
    #    self.assertEqual(divide(20, 5), 4)

class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(-6))
        self.assertTrue(is_even(220))
        self.assertTrue(not is_even(-3))
        self.assertTrue(not is_even(57))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(57))

class TestDivide(unittest.TestCase):

    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)
        self.assertRaises(TypeError, divide, 6, 'a')

if __name__ == '__main__':
    unittest.main()