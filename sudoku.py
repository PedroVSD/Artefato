import random

def generate_sudoku():
    # Cria uma matriz vazia de 9x9
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    # Preenche a matriz com números válidos de Sudoku
    solve_sudoku(sudoku)

    # Remove alguns números aleatoriamente para criar o jogo
    remove_numbers(sudoku)

    return sudoku

def solve_sudoku(sudoku):
    # Encontra a próxima célula vazia
    row, col = find_empty_cell(sudoku)

    # Se não houver mais células vazias, o Sudoku está resolvido
    if row == -1 and col == -1:
        return True

    # Tenta preencher a célula vazia com um número válido
    for num in range(1, 10):
        if is_valid_number(sudoku, row, col, num):
            sudoku[row][col] = num

            # Chama recursivamente a função para preencher as células restantes
            if solve_sudoku(sudoku):
                return True

            # Se a recursão falhar, desfaz a atribuição e tenta outro número
            sudoku[row][col] = 0

    # Se nenhum número válido for encontrado, o Sudoku não tem solução
    return False

def find_empty_cell(sudoku):
    # Encontra a próxima célula vazia na matriz
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col
    return -1, -1

def is_valid_number(sudoku, row, col, num):
    # Verifica se o número é válido na linha
    for i in range(9):
        if sudoku[row][i] == num:
            return False

    # Verifica se o número é válido na coluna
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # Verifica se o número é válido no bloco 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True

def remove_numbers(sudoku):
    # Remove alguns números aleatoriamente para criar o jogo
    empty_cells = random.sample(range(81), 50)
    for cell in empty_cells:
        row = cell // 9
        col = cell % 9
        sudoku[row][col] = 0

def print_sudoku(sudoku):
    # Imprime o Sudoku formatado
    for row in sudoku:
        print(' '.join(map(str, row)))

# Gera um jogo de Sudoku
sudoku = generate_sudoku()

# Imprime o jogo
print("Jogo:")
print_sudoku(sudoku)

# Imprime a resposta
print("Resposta:")
print_sudoku(sudoku)