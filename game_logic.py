import random

class GameLogic:
    def __init__(self):
        self.choices = {1: "FROG", 2: "SLUG", 3: "SNAKE"}
        self.player_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.randint(1, 3)

    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a tie!"
        elif (
            (player == 1 and computer == 3) or
            (player == 2 and computer == 1) or
            (player == 3 and computer == 2)
        ):
            self.player_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Rival Chairman wins!"