import random
import time

class Card:
    def __init__(self, value):
        self.value = value
        self.face_up = False

    def flip(self):
        self.face_up = not self.face_up

class Board:
    def __init__(self, size):
        self.size = size
        self.cards = [Card(i) for i in range(size//2) for _ in range(2)]
        random.shuffle(self.cards)

    def display(self):
        for i, card in enumerate(self.cards):
            if card.face_up:
                print(f"{card.value:2}", end=" ")
            else:
                print(" *", end=" ")
            if (i + 1) % (self.size // 2) == 0:
                print()
        print()

class GameState:
    def __init__(self):
        self.turns = 0
        self.pairs_found = 0

class Timer:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def is_time_up(self):
        if self.start_time is None:
            return False
        return time.time() - self.start_time > self.time_limit

    def remaining_time(self):
        if self.start_time is None:
            return self.time_limit
        return max(0, self.time_limit - (time.time() - self.start_time))

class MemoryGame:
    def __init__(self, size):
        self.board = Board(size)
        self.state = GameState()

    def play(self):
        while self.state.pairs_found < self.board.size // 2:
            self.display_game_state()
            self.take_turn()
        self.end_game()

    def display_game_state(self):
        self.board.display()

    def take_turn(self):
        index1, index2 = self.get_card_indices()
        self.flip_cards(index1, index2)
        self.board.display()
        self.check_match(index1, index2)
        self.state.turns += 1

    def get_card_indices(self):
        index1 = int(input("Enter the index of the first card: "))
        index2 = int(input("Enter the index of the second card: "))
        return index1, index2

    def flip_cards(self, index1, index2):
        self.board.cards[index1].flip()
        self.board.cards[index2].flip()

    def check_match(self, index1, index2):
        if self.board.cards[index1].value == self.board.cards[index2].value:
            print("Match found!")
            self.state.pairs_found += 1
        else:
            print("No match. Try again.")
            self.board.cards[index1].flip()
            self.board.cards[index2].flip()

    def end_game(self):
        print(f"Congratulations! You completed the game in {self.state.turns} turns.")

class TimedMemoryGame():
    def __init__(self, size, time_limit):
        self.memory_game = MemoryGame(size)
        self.timer = Timer(time_limit)

    def play(self):
        self.timer.start()
        while self.memory_game.state.pairs_found < self.memory_game.board.size // 2 and not self.timer.is_time_up():
            self.display_game_state()
            self.memory_game.take_turn()
        self.end_game()

    def display_game_state(self):
        self.memory_game.display_game_state()
        print(f"Time remaining: {self.timer.remaining_time():.1f} seconds")

    def end_game(self):
        if self.timer.is_time_up():
            print(f"Time's up! You found {self.state.pairs_found} pairs in {self.state.turns} turns.")
        else:
            elapsed_time = self.timer.time_limit - self.timer.remaining_time()
            print(f"Congratulations! You completed the game in {self.state.turns} turns and {elapsed_time:.1f} seconds.")


# Usage
print("Regular Memory Game:")
# regular_game = MemoryGame(8)
# regular_game.play()

print("\nTimed Memory Game:")
timed_game = TimedMemoryGame(8, 60)  # 8 cards, 60 seconds time limit
timed_game.play()