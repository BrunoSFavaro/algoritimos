nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

p= n*-1
j= 0
for i in range(m):
  nums1[p] = nums2[j]
  p = p + 1
  j = j + 1

nums1.sort()

print (nums1)