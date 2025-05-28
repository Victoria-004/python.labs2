import unittest
from wchain import *


class TestWChain(unittest.TestCase):
    def test_example1(self):
        with open('wchain.in', 'w') as f:
            f.write('10\ncrates\ncar\ncats\ncrate\nrate\nat\nate\ntea\nrat\na\n')

        solve('wchain.in', 'wchain.out')
        with open('wchain.out', 'r') as f:
            result = int(f.readline())
        self.assertEqual(result, 6)

    def test_long_chain(self):
        with open('wchain.in', 'w') as f:
            f.write('11\nvicky\nvika\nvictoria\nvi\nvictori\ntori\nictori\nctori\ntor\nor\nr\n')

        solve('wchain.in', 'wchain.out')

        with open('wchain.out', 'r') as f:
            result = int(f.readline())
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()