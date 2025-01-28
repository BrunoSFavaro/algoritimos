def maior_sequencia_sem_repeticao(string):
    maior_seq = 0  # Para armazenar o maior tamanho encontrado
    for i in range(len(string)):  # Percorre cada posição da string
        sequencia = ""  # Sequência atual sem repetição
        for j in range(i, len(string)):  # Percorre a partir do índice atual
            if string[j] not in sequencia:  # Se o caractere não estiver na sequência
                sequencia += string[j]  # Adiciona o caractere à sequência
            else:
                break  # Para o loop quando encontrar uma repetição
        maior_seq = max(maior_seq, len(sequencia))  # Atualiza o maior tamanho encontrado
    return maior_seq

# Exemplo de uso
string = "pwwkew"
print(maior_sequencia_sem_repeticao(string))  # Saída: 3
