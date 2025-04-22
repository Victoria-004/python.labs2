import unittest
from tribes import find_connected_components, calc_tribe_pairs

class TestTribePairing(unittest.TestCase):
    def test_find_connected_components1(self):
        n = 4
        tribe_pairs = [("1", "2"), ("2", "3"), ("4", "5"), ("5", "6")]
        expected_components = [{1, 2, 3}, {4, 5, 6}]
        self.assertEqual(find_connected_components(n, tribe_pairs), expected_components)

    def test_find_connected_components2(self):
        n = 3
        tribe_pairs = [("1", "2"), ("2", "4"), ("3", "5")]
        expected_components = [{1, 2, 4}, {3, 5}]
        self.assertEqual(find_connected_components(n, tribe_pairs), expected_components)

    def test_find_connected_components3(self):
        n = 5
        tribe_pairs = [("1", "2"), ("2", "4"), ("1", "3"), ("3", "5"), ("8", "10")]
        expected_components = [{1, 2, 3, 4, 5}, {8, 10}]
        self.assertEqual(find_connected_components(n, tribe_pairs), expected_components)


if __name__ == '__main__':
    unittest.main()