import unittest

def sorted_squares(nums):
  squared_nums = [x ** 2 for x in nums]
  return sorted(squared_nums)

class TestSortedSquaresFunc(unittest.TestCase):

  def test_squares_func(self):
    self.assertEqual(sorted_squares([-4,-2,0,1,3]), [0,1,4,9,16])
    self.assertEqual(sorted_squares([1,2,3,4,5]), [1,4,9,16,25])

if __name__ == '__main__':
  unittest.main()
