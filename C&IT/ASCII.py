import re

def seven_segmentify(time_str: str) -> str:
    # Extrair o horário no formato "HH:MM" da string
    match = re.search(r"\d{2}:\d{2}", time_str)
    if not match:
        return "Formato inválido"

    time = match.group(0)
    hours, minutes = time.split(':')
    if hours[0] == "0": #Tratando os zeros à esquerda
      hours = " " + hours[1:] #Colocando um espaço no lugar do zero à esquerda e mantendo o resto do horário
    else:
      hours = hours.lstrip('0')  # Remover zero à esquerda da hora

    display = ["", "", ""]  # Inicializar a exibição ASCII

    for part in [hours, minutes]:
        for i in range(len(part)):
            digit = part[i]
            for row in range(3):
                # Concatena os dígitos
                display[row] += digitos[digit][row]

        # Adicionar os pontos ":" para formar o relógio entre horas e minutos
        if part == hours:
            display[0] += "   "  # Linha superior do ":"
            display[1] += " . "  # Linha do meio do ":"
            display[2] += " . "  # Linha inferior do ":"

    return "\n".join(display)

digitos = {
  '0' : [" _ ", "| |", "|_|"],
  '1' : ["   ", "  |", "  |"],
  '2' : [" _ ", " _|", "|_ "],
  '3' : [" _ ", " _|", " _|"],
  '4' : ["   ", "|_|", "  |"],
  '5' : [" _ ", "|_ ", " _|"],
  '6' : [" _ ", "|_ ", "|_|"],
  '7' : [" _ ", "  |", "  |"],
  '8' : [" _ ", "|_|", "|_|"],
  '9' : [" _ ", "|_|", " _|"],
  ' ' : ["   ", "   ", "   "] #Adicionado para tratamento do zero à esquerda
}

time = str(input())
print(seven_segmentify(time))

