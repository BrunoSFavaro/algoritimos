# Dicionário que mapeia combinações de código Morse para letras

# Função interna para expandir combinações substituindo '?' por '.' e '-'
def expand_combinations(morse_code):
    # Se não há '?', a string já é válida e retorna apenas ela mesma
    if "?" not in morse_code:
        return [morse_code]
    
    # Lista para armazenar as combinações geradas
    combinations = [morse_code]  # Começamos com a palavra original
    
    # Itera sobre cada caractere de morse_code
    for i in range(len(morse_code)):
        # Verifica se encontramos um '?', indicando que precisamos gerar possibilidades
        if morse_code[i] == "?":
            # Cria uma nova lista de combinações substituindo '?' por '.' e '-'
            new_combinations = []
            # Para cada combinação existente, substituímos '?' por '.' e '-'
            for combo in combinations:
                # Substitui '?' por '.' e adiciona a nova combinação
                new_combinations.append(combo[:i] + "." + combo[i+1:])
                # Substitui '?' por '-' e adiciona a nova combinação
                new_combinations.append(combo[:i] + "-" + combo[i+1:])
            # Atualiza as combinações com as novas geradas
            combinations = new_combinations
    
    # Retorna todas as combinações gerad'as para a string de morse_code
    return combinations

def translate(morse):
    # Usa expand_combinations para obter todas as possibilidades
    possibilities = expand_combinations(morse)

    # Filtra apenas as combinações válidas no dicionário Morse e retorna suas letras
    results = [morse_dict.get(code) for code in possibilities if code in morse_dict]
    return results


morse_dict = {
    ".": "E",
    "-": "T",
    "..": "I",
    ".-": "A",
    "-.": "N",
    "--": "M",
    "...": "S",
    "..-": "U",
    ".-.": "R",
    ".--": "W",
    "-..": "D",
    "-.-": "K",
    "--.": "G",
    "---": "O",
}
# Exemplo de uso
codigo = input()
resultado = translate(codigo)
print("Possíveis resultados:", resultado)
