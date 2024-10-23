import sys

# Inserindo valores
try:
    v1 = float(input("Insira o primeiro lado do triângulo: "))
    v2 = float(input("Insira o segundo lado do triângulo: "))
    v3 = float(input("Insira o terceiro lado do triângulo: "))
except ValueError:
    print("Os lados do triângulo precisam ser numéricos.")
    sys.exit()  # Termina o programa caso ocorra erro de entrada

# Verificando se os lados são positivos
if v1 <= 0 or v2 <= 0 or v3 <= 0:
    print("Os lados do triângulo devem ser números maiores que 0.")
    sys.exit()

# Ordenando os valores de forma crescente para facilitar os testes
if v1 > v2:
    v1, v2 = v2, v1  # Swap
if v2 > v3:
    v2, v3 = v3, v2  # Swap
if v1 > v2:
    v1, v2 = v2, v1  # Swap

# Verificação de triângulo degenerado (quando a soma de dois lados é igual ao terceiro)
if v1 + v2 == v3:
    print("Os valores inseridos formam um triângulo degenerado (linha reta).")
    sys.exit()

# Fórmula para validar o triângulo (a soma dos dois menores lados deve ser maior que o terceiro)
if v1 + v2 < v3:
    print("Os valores inseridos não formam um triângulo.")
else:
    # Testes para verificar qual o tipo de triângulo
    if v1 == v2 == v3:
        print("Os valores inseridos formam um triângulo equilátero.")
    elif v1 == v2 or v2 == v3:
        print("Os valores inseridos formam um triângulo isósceles.")
    else:
        print("Os valores inseridos formam um triângulo escaleno.")
