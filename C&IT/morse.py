#Mapeamento das letras a serem usadas no desafio
dicionario = {
    ".": "E",
    "..": "I",
    "...": "S",
    "..-": "U",
    ".-": "A",
    ".-.": "R",
    ".--": "W",
    "-": "T",
    "-.": "N",
    "-..": "D",
    "-.-": "K",
    "--": "M",
    "--.": "G",
    "---": "O"
}

def combinations(morse_code):
    if "?" not in morse_code:
        return [morse_code]     #Retorna o código original se não houver "?"
    
    return combinations



def morse_to_text(morse_code):
    possibilities = combinations(morse_code) #Usa a outra função para encontrar as possíveis combinações
    results = [dicionario.get(code) for code in possibilities if code in dicionario] #Filtra as combinações que existem no dicionário
    return results

codigo = input()
resultado = morse_to_text(codigo)
print(resultado)