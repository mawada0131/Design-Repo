import random
from card import Card


class Board:
    def __init__(self, size):
        self.size = size
        self.cards = [Card(i) for i in range(size//2) for _ in range(2)] #פונקציה לבד
        random.shuffle(self.cards)
        self.pairs_found = 0

    def check_match(self,index1,index2):
        if self.cards[index1].value == self.cards[index2].value:
                print("Match found!")
                self.pairs_found += 1
        else:
            print("No match. Try again.")
            self.cards[index1].flip()
            self.cards[index2].flip()
        

    def getIndex(self): #check valid index
        index1 = int(input("Enter the index of the first card: "))
        index2 = int(input("Enter the index of the second card: "))
        return index1,index2
    
    def play(self):
        turns = 0
        self.pairs_found = 0

        while self.pairs_found < self.size // 2:
            self.display_board()
            
            index1, index2 = self.getIndex()

            self.cards[index1].flip()
            self.cards[index2].flip()

            self.display_board()
            self.check_match(index1,index2)

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