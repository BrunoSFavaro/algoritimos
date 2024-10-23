N = int(input())
cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
test = 1
while(test):
    if(N >= 100):
        cem += 1
        N -= 100
    elif(N >= 50):
        cinq += 1
        N -= 50
    elif(N >= 20):
        vinte += 1
        N -= 20
    elif(N >= 10):
        dez += 1
        N -= 10
    elif(N >= 5):
        cinco += 1
        N -= 5
    elif(N >= 2):
        dois += 1
        N -= 2
    elif(N >= 1):
        um += 1
        N -= 1
    else:
        test = 0

print(f"{cem} nota(s) de R$ 100,00\n{cinq} nota(s) de R$ 50,00\n{vinte} nota(s) de R$ 20,00\n{dez} nota(s) de R$ 10,00\n{cinco} nota(s) de R$ 5,00\n{dois} nota(s) de R$ 2,00\n{um} nota(s) de R$ 1,00")
    