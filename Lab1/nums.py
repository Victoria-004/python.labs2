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

array1 = sorted_squares([1, 2, 3, 4, 5])
array2 = sorted_squares([-6, -4, 0, 2, 11])
print(array1)
print(array2)

