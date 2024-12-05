def josephus_iterative(n, k):
    sobrevivente = 0 
    for i in range(2, n + 1):
        sobrevivente = (sobrevivente + k) % i
    return sobrevivente

NC = int(input())

resultados = []

for _ in range(NC):
    n, k = map(int, input().split())
    sobrevivente = josephus_iterative(n, k) + 1 
    resultados.append(sobrevivente) 


for i, res in enumerate(resultados, start=1):
    print(f"Case {i}: {res}")