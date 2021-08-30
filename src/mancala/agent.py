import random
import time


class RandomAgent:

    def __init__(self, player_side):
        self.player_side = player_side

    def get_state_of_game(self, state):
        hole_i = random.choice(possible_holes).hole_i
        print(f'RandomAgent selects: {hole_i}')
        time.sleep(10)
        return self.player_side, hole_i


class HumanAgent:

    actions = []
    states = []

    def __init__(self, player_side):
        self.player_side = player_side
