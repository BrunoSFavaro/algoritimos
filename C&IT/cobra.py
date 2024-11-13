def snake_coordinates(grid):
    # Dimensões da matriz
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0

    # Contar segmentos da cobra (qualquer caractere que não seja espaço em branco)
    total_segments = sum(1 for row in grid for char in row if char != ' ')

    # Encontrar a cabeça da cobra (h)
    head_x, head_y = None, None
    for y in range(num_rows):
        for x in range(num_cols):
            if grid[y][x] == 'h':
                head_x, head_y = x, y
                break
        if head_x is not None:
            break

    # Se não encontrou a cabeça, retorna uma lista vazia
    if head_x is None:
        return []

    # Lista para armazenar as coordenadas da cobra
    coordinates = []  
    coordinates.append([head_x, head_y])

    # Dicionário de direções com seus deslocamentos
    directions = {
        '>': (-1, 0),   # direita
        '<': (1, 0),    # esquerda
        '^': (0, 1),   # cima
        'v': (0, -1)     # baixo
    }

    # Posicionar a partir da cabeça e seguir os segmentos até o total necessário
    current_x, current_y = head_x, head_y
    while len(coordinates) < total_segments:
        found_next_segment = False

        # Explorar as posições adjacentes em todas as direções possíveis
        for symbol, (dx, dy) in directions.items():
            next_x, next_y = current_x + dx, current_y + dy
            if (
                0 <= next_x < num_cols and
                0 <= next_y < num_rows and
                grid[next_y][next_x] == symbol and
                [next_x, next_y] not in coordinates
            ):
                # Encontrou o próximo segmento, adiciona às coordenadas
                coordinates.append([next_x, next_y])
                # Atualiza a posição atual para o próximo segmento
                current_x, current_y = next_x, next_y
                found_next_segment = True
                break  # Para evitar múltiplas adições por direção

        # Se não encontrou próximo segmento, interrompe o loop
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
