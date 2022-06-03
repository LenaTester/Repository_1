import unittest
from funcs import is_even, is_odd, custom_max, multiply, reverse, upper_count, unique, is_pangram

class IsEvenTestCase(unittest.TestCase):

    def test_ten(self):
        self.assertTrue(is_even(10), "10 should be even")

    def test_one(self):
        self.assertFalse(is_even(1), "1 shouldn't be even")

    def test_exception(self):
        with self.assertRaises(TypeError):
            is_even("10")

class IsOddTestCase(unittest.TestCase):

    def test_eleven(self):
        self.assertTrue(is_odd(11), "11 should be odd")

    def test_twelve(self):
        self.assertFalse(is_odd(12), "12 shouldn't be odd")

    def test_exception(self):
        with self.assertRaises(TypeError):
            is_odd('some text')

class CustomMaxTestCase(unittest.TestCase):

    def test_a_is_greater(self):
        self.assertEqual(custom_max(10, 5), 10, "10 is greater, than 5")

    def test_b_is_greater(self):
        self.assertEqual(custom_max(1, 100), 100, "100 is greater, than 1")

    def test_exception(self):
        with self.assertRaises(TypeError):
            custom_max("some text")

class MultiplyTestCase(unittest.TestCase):

    def test_multiply_base_1(self):
        self.assertEqual(multiply(*list(range(1, 10)), base=1), 362880, "the correct answer is 362880")

    def test_multiply_base_2(self):
        self.assertEqual(multiply(*list(range(1, 10)), base=2), 725760, "the correct answer is 725760")

    def test_exception(self):
        with self.assertRaises(TypeError):
            multiply("some text", base='some string')

class ReverseTestCase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse(""), "", "reversed string does not contain any symbols")

    def test_long_string(self):
        self.assertEqual(reverse("QWERqwer123!@#"), "#@!321rewqREWQ", "reversed string is #@!321rewqREWQ")

    def test_exception(self):
        with self.assertRaises(TypeError):
            reverse(8.568)

class UpperCountTestCase(unittest.TestCase):

    def test_empty_string_upper_count(self):
        self.assertEqual(upper_count(""), 0, "reversed string contains 0 upper case symbols")

    def test_long_string_upper_count(self):
        self.assertEqual(upper_count("QWER qwer 123 !@#"), 4, "reversed string contains 4 upper case symbols")

    def test_exception(self):
        with self.assertRaises(TypeError):
            upper_count(8.568)

class UniqueTestCase(unittest.TestCase):

    def test_unique_list_seven_elements(self):
        self.assertEqual(unique([2, 2, 1, 5, 5, 2, 7]), [1, 2, 5, 7], "correct result is: [1, 2, 5, 7]")

    def test_unique_list_three_elements(self):
        self.assertEqual(unique([1, 1, 1]), [1], "correct result is: [1]")

    def test_exception(self):
        with self.assertRaises(TypeError):
            unique(9.5959)

class IsPangramTestCase(unittest.TestCase):

    def test_pangram(self):
        self.assertTrue(is_pangram("The five boxing wizards jump quickly"), "this is a pangram")

    def test_non_pangram(self):
        self.assertFalse(is_pangram('Today is Wednesday'), "this is not a pangram")

    def test_exception(self):
        with self.assertRaises(AttributeError):
            is_pangram(99.99)