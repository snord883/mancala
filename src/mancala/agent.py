import random
import time


class MancalaAgent:

    def __init__(self, player_side):
        self.player_side = player_side
        self.actions = []
        self.states = []
        self.games = []

    def get_state_of_game(self, holes, scoreboard):
        tmp_state = []
        for player_idx in (self.player_side, not self.player_side):
            for hole in holes[player_idx]:
                tmp_state.append(hole.n_marbles)
            tmp_state.append(scoreboard[player_idx].n_marbles)
        print(tmp_state)
        self.states.append(tmp_state)
        print(f"PLAYER {self.player_side} STATES: {self.states}")

    # def get_results_of_game(self, scoreboard):



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
