import random
import time


class MancalaAgent:

    actions = []
    states = []
    games = []

    def __init__(self, player_side):
        self.player_side = player_side

    def get_state_of_game(self, holes, scoreboard):
        tmp_state = []


class RandomAgent(MancalaAgent):

    def __init__(self, player_side):
        super().__init__(player_side)
        self.player_side = player_side

    def select_from_possible_holes(self, holes):
        time.sleep(.5)
        return self.player_side, random.choice(holes)


class HumanAgent(MancalaAgent):

    def __init__(self, player_side):
        super().__init__(player_side)
        self.player_side = player_side
