import unittest
from task import search_last_index, number_of_comparisons

class TestSearchLastIndex(unittest.TestCase):

    def test_needle_found_once(self):
        haystack = 'HelloWorld'
        needle = 'ello'
        last_index, number_of_comparisons = search_last_index(haystack, needle)
        self.assertEqual(last_index, 4)
        self.assertEqual(number_of_comparisons, 10)

    def test_needle_found_multiple_times(self):
        haystack = "abcdabcd"
        needle = "b"
        last_index, number_of_comparisons = search_last_index(haystack, needle)
        self.assertEqual(last_index, 5)
        self.assertEqual(number_of_comparisons, 8)

if __name__ == '__main__':
    unittest.main()