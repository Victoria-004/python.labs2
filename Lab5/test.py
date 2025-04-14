import unittest
from min_depth import read_file, min_depth

class TestMinDepthExistingFile(unittest.TestCase):

    def test_input_file(self):
        try:
            root, tree = read_file("input.txt")
            expected_depth = 3
            self.assertEqual(min_depth(root, tree), expected_depth)
        except FileNotFoundError:
            self.fail("File input.txt is not found.")

if __name__ == '__main__':
    unittest.main()