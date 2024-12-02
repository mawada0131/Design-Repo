import random

def initialize_board():
    numbers = list(range(1, (8 * 8) + 1))  
    random.shuffle(numbers)  
    board = []
    
    for i in range(8):
        board.append(numbers[i * 8:(i + 1) * 8])
    
    return board

# Example usage
board = initialize_board()
for row in board:
    print(row)
