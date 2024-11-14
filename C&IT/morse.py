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
         #Lista para armazenar as combinações possíveis
    combinations = []
    for char in morse_code:
        #Se o caractere é "?", cria combinações com "." e "-"
        if char == "?":
            if not combinations:            #Combionations vazio
                combinations = [".", "-"]   #Inicializa com as duas possibilidades para '?'
            else:
                combinations = [combo + "." for combo in combinations] +  [combo + "-" for combo in combinations] #Expande cada combinação já existente com '.' e '-'
        #Se o caractere não for '?'
        else:
            #E combinations estiver vazio
            if not combinations:
                #Inicializa com o caractere
                combinations = [char]
            #Se combinations não estiver vazio
            else:
                #Adiciona o caractere a cada combinação já existente
                combinations = [combo + char for combo in combinations]

    
    return combinations



def morse_to_text(morse_code):
    possibilities = combinations(morse_code) #Usa a outra função para encontrar as possíveis combinações
    results = [dicionario.get(code) for code in possibilities if code in dicionario] #Filtra as combinações que existem no dicionário
    return results

codigo = input()
resultado = morse_to_text(codigo)
print(resultado)