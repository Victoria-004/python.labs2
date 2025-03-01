def sorted_squares(nums):
  squared_nums = [x ** 2 for x in nums]
  return sorted(squared_nums)

array1 = sorted_squares([1, 2, 3, 4, 5])
array2 = sorted_squares([-6, -4, 0, 2, 11])
print(array1)
print(array2)

