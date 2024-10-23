T = int(input())
if(T < 1 or T > 4):
    print("Valor inserido é inválido")
else:
    print(sum([1 if int(n) == T else 0 for n in input().split()]))

    # count = 0
    # for numero in numeros:
    #     if(numero == T):
    #         count += 1
    
    # print(count)
        