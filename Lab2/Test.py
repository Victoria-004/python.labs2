import unittest
from poker import longest_sequence

class TestLongestSequence(unittest.TestCase):
    def test_longest_sequence_func(self):
        self.assertEqual(longest_sequence([0, 10, 15, 50, 0, 14, 9, 12, 40]), 7)

    def test_longest_sequence_func2(self):
        self.assertEqual(longest_sequence([1, 1, 1, 2, 1, 1, 3]), 3)

    def test_longest_sequence_func3(self):
        self.assertEqual(longest_sequence([5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 0, 0]), 4)

if __name__ == '__main__':
    unittest.main()
