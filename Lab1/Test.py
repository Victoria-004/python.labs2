import unittest

def bubble_sort(array):
  n = len(array)
  for i in range(n):
    for j in range(0, n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
  return array

def sorted_squares(nums):
  squared_nums = [x ** 2 for x in nums]
  return bubble_sort(squared_nums)

class TestSortedSquaresFunc(unittest.TestCase):

  def test_squares_func(self):
    self.assertEqual(sorted_squares([-4,-2,0,1,3]), [0,1,4,9,16])
    self.assertEqual(sorted_squares([1,2,3,4,5]), [1,4,9,16,25])

if __name__ == '__main__':
  unittest.main()
