nums = [2,7,11,15]
target = 9

visto = {}

for i, num in enumerate(nums):
  complemento = target - num
  if complemento in visto:
    print(visto[complemento], i)
  visto[num] = i

