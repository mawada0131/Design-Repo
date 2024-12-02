import random
from card import Card


class Board:
    def __init__(self, size):
        self.size = size
        self.cards = [Card(i) for i in range(size//2) for _ in range(2)]
        random.shuffle(self.cards)

    def play(self):
        turns = 0
        pairs_found = 0

        while pairs_found < self.size // 2:
            self.display_board()
            
            index1 = int(input("Enter the index of the first card: "))
            index2 = int(input("Enter the index of the second card: "))

            self.cards[index1].flip()
            self.cards[index2].flip()

            self.display_board()

            if self.cards[index1].value == self.cards[index2].value:
                print("Match found!")
                pairs_found += 1
            else:
                print("No match. Try again.")
                self.cards[index1].flip()
                self.cards[index2].flip()

            turns += 1

        print(f"Congratulations! You completed the game in {turns} turns.")

    def display_board(self):
        for i, card in enumerate(self.cards):
            if card.face_up:
                print(f"{card.value:2}", end=" ")
            else:
                print(" *", end=" ")
            if (i + 1) % (self.size // 2) == 0:
                print()
        print()

# Example usage
board_size = 4
game = Board(board_size)  
game.play()