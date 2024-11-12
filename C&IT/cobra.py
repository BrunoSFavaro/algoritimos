def snake_coordinates(grid):
    # Encontrar a cabeça da cobra (h)
    head_x, head_y = None, None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'h':
                head_x, head_y = x, y
                break
        if head_x is not None:
            break

    # Se não encontrou a cabeça, retorna uma lista vazia
    if head_x is None:
        return []

    # Lista para armazenar as coordenadas da cobra
    coordinates = [[head_x, head_y]]

    # Dicionário de direções com seus deslocamentos
    directions = {
        '>': (1, 0),  # direita
        '<': (-1, 0), # esquerda
        '^': (0, -1), # cima
        'v': (0, 1)   # baixo
    }

    # Posicionar a partir da cabeça e seguir os segmentos até a cauda
    current_x, current_y = head_x, head_y
    while True:
        found_next_segment = False

        # Explorar as posições adjacentes em todas as direções possíveis
        for symbol, (dx, dy) in directions.items():
            next_x, next_y = current_x + dx, current_y + dy
            if (
                0 <= next_x < len(grid[0]) and
                0 <= next_y < len(grid) and
                grid[next_y][next_x] == symbol
            ):
                # Encontrou o próximo segmento, adiciona às coordenadas
                coordinates.append([next_x, next_y])
                # Atualiza a posição atual para o próximo segmento
                current_x, current_y = next_x, next_y
                found_next_segment = True
                break

        # Se não encontrou próximo segmento, chegamos à cauda
        if not found_next_segment:
            break

    return coordinates

# Exemplo de grid
grid = [
    ">>v",
    "^h<",
    "^<<",
]

print(snake_coordinates(grid))
