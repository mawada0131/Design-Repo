import random

def initialize_board(numbers,n):
    random.shuffle(numbers).seed(23)
    board = []
    for i in range(n):
        board.append(numbers[i * n:(i + 1) * n])
    
    return board

# Example usage
board_dim = 8
numbers = list(range(1, (8 * 8) + 1)) 
board = initialize_board(numbers,board_dim)
for row in board:
    print(row)
