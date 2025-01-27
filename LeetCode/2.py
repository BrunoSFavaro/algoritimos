l1 = [2, 4, 3]
l2 = [5, 6, 4]

result = []
add = 0 

for i in range(len(l1)):
    soma = l1[i] + l2[i] + add
    add = soma // 10
    result.append(soma % 10) 
    
if add:
    result.append(add)

print(result)
