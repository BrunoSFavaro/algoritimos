import math

nums1 = [1,3]
nums2 = [2]

array = nums1 + nums2
array.sort()
i = len(array)
if i % 2 != 0:
  x = math.floor(i/2)
  print(array[x])
else:
  x = i/2
  x = int(x)
  x = (array[x] + array[x-1]) / 2
  print(x)