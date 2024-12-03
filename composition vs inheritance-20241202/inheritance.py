import random
import time

class Card:
    def __init__(self, value):
        self.value = value
        self.face_up = False

    def flip(self):
        self.face_up = not self.face_up

class MemoryGame:
    def __init__(self, size):
        self.size = size
        self.cards = [Card(i) for i in range(size//2) for _ in range(2)]
        random.shuffle(self.cards)
        self.turns = 0
        self.pairs_found = 0

    def play(self):
        while self.pairs_found < self.size // 2:
            self.display_game_state()
            self.take_turn()
        self.end_game()

    def display_game_state(self):
        self.display_board()

    def display_board(self):
        for i, card in enumerate(self.cards):
            if card.face_up:
                print(f"{card.value:2}", end=" ")
            else:
                print(" *", end=" ")
            if (i + 1) % (self.size // 2) == 0:
                print()
        print()

    def take_turn(self):
        index1, index2 = self.get_card_indices()
        self.flip_cards(index1, index2)
        self.display_board()
        self.check_match(index1, index2)
        self.turns += 1

    def get_card_indices(self):
        index1 = int(input("Enter the index of the first card: "))
        index2 = int(input("Enter the index of the second card: "))
        return index1, index2

    def flip_cards(self, index1, index2):
        self.cards[index1].flip()
        self.cards[index2].flip()

    def check_match(self, index1, index2):
        if self.cards[index1].value == self.cards[index2].value:
            print("Match found!")
            self.pairs_found += 1
        else:
            print("No match. Try again.")
            self.cards[index1].flip()
            self.cards[index2].flip()

    def end_game(self):
        print(f"Congratulations! You completed the game in {self.turns} turns.")

class TimedMemoryGame(MemoryGame):
    def __init__(self, size, time_limit):
        super().__init__(size)
        self.time_limit = time_limit
        self.start_time = None

    def play(self):
        self.start_time = time.time()
        while self.pairs_found < self.size // 2 and not self.is_time_up():
            self.display_game_state()
            self.take_turn()
        self.end_game()

    def is_time_up(self):
        elapsed_time = time.time() - self.start_time
        return elapsed_time > self.time_limit

    def display_game_state(self):
        super().display_game_state()
        remaining_time = max(0, self.time_limit - (time.time() - self.start_time))
        print(f"Time remaining: {remaining_time:.1f} seconds")

    def end_game(self):
        elapsed_time = time.time() - self.start_time
        if self.pairs_found == self.size // 2:
            print(f"Congratulations! You completed the game in {self.turns} turns and {elapsed_time:.1f} seconds.")
        else:
            print(f"Time's up! You found {self.pairs_found} pairs in {self.turns} turns.")

# Usage
print("Regular Memory Game:")
game = MemoryGame(8)
game.play()

print("\nTimed Memory Game:")
timed_game = TimedMemoryGame(8, 30)  # 8 cards, 60 seconds time limit
timed_game.play()