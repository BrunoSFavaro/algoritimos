import numpy as np

# sequencia em python 
python_list = [i for i in range(1_000_000 + 1)]


# sequencia numpy 
numpy_list = np.arange(0, 1_000_000 + 1, dtype='int64')

# Quadrados no python
python_list_square = [i**2 for i in python_list]

# Quadrados no numpy
numpy_list_square = numpy_list**2

#array no numpy
arr = np.array([1, 2, 3, 4, 5])
print(f"Elementos: {arr}, Tipo dos elementos: {arr.dtype}, Tamanho do array: {arr.shape}")

elemento = arr[2]
print(elemento)

#Obtendo elementos do índice 1 a 3
subset = arr[1:4]
print(subset)

#Criando matriz
matrix = np.arange(1., 10.).reshape((3, 3))
print(matrix)
print(f"Tipo dos elementos: {matrix.dtype}, Dimensões da matriz: {matrix.shape}")

#Acessando uma linha específica na matriz
linha = matrix[1]
print(linha)

#Acessando uma coluna específica na matriz
coluna = matrix[:, 1]
print(coluna)

mult = 2.0
resultado = matrix * mult
print(resultado)

#Multiplicando matrizes
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[1], [2]])

#Multiplicação usando apenas as listas do python
C = [[0], [0], [0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

print(C)


#Agora utilizando NumPy
D = A @ B
print(D)


N = 500

A = np.arange(N*N, dtype='int64').reshape(N, N)
B = A * 2

C = A @ B
print(C)