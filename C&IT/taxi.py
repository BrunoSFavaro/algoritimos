# Função para formatar o número com 1 ou 2 casas decimais
def formatar_numero(valor):
    if round(valor, 1) == round(valor, 2):
        return f"{valor:.1f}"
    else:
        return f"{valor:.2f}"

# Valores de entrada
TF1 = 3.5
VQR1 = 1.0
TF2 = 3
VQR2 = 1.0

# Converter entradas para float, caso necessário
TF1, VQR1, TF2, VQR2 = map(float, [TF1, VQR1, TF2, VQR2])

# Calcular a diferença nas taxas fixas e valores por quilômetro
TFDif = TF1 - TF2
VQRDif = VQR1 - VQR2

# Condições para decidir o resultado
if TFDif == 0 and VQRDif == 0:
    # Caso em que as taxas e valores por quilômetro são iguais
    resultado = "Tanto faz"
elif TFDif <= 0 and VQRDif <= 0:
    # Empresa 1 é sempre mais barata
    resultado = "Empresa 1"
elif TFDif >= 0 and VQRDif >= 0:
    # Empresa 2 é sempre mais barata
    resultado = "Empresa 2"
elif VQRDif == 0:
    # Caso em que os valores por quilômetro são iguais, mas taxas fixas diferem
    resultado = "Empresa 1" if TFDif < 0 else "Empresa 2"
else:
    # Calcular a distância onde os preços se igualam
    equal = abs(TFDif / VQRDif)
    equal_formatado = formatar_numero(equal)  # Formatando o equal

    # Verificar qual empresa é melhor abaixo e acima da distância de equilíbrio
    if TFDif / VQRDif > 0:
        # Empresa 1 é mais barata para distâncias menores, Empresa 2 para maiores
        resultado = f"Empresa 2 quando a distância < {equal_formatado}, Tanto faz quando a distância = {equal_formatado}, Empresa 1 quando a distância > {equal_formatado}"
    else:
        # Empresa 2 é mais barata para distâncias menores, Empresa 1 para maiores
        resultado = f"Empresa 1 quando a distância < {equal_formatado}, Tanto faz quando a distância = {equal_formatado}, Empresa 2 quando a distância > {equal_formatado}"

# Imprimir o resultado
print(resultado)
