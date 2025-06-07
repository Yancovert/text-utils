import unittest
from text_utils.cleaner import remove_extra_spaces
from text_utils.converter import to_uppercase, to_lowercase, reverse_text
from text_utils.counter import count_words, count_characters, count_lines

class TestUtils(unittest.TestCase):
    def test_cleaner(self):
        self.assertEqual(remove_extra_spaces("this   is  test"), "this is test")

    def test_converter(self):
        self.assertEqual(to_uppercase("test"), "TEST")
        self.assertEqual(to_lowercase("TEST"), "test")
        self.assertEqual(reverse_text("abc"), "cba")

    def test_counter(self):
        sample = "hello world\nthis is test"
        self.assertEqual(count_words(sample), 5)
        self.assertEqual(count_characters(sample), len(sample))
        self.assertEqual(count_lines(sample), 2)

if __name__ == "__main__":
    unittest.main()
