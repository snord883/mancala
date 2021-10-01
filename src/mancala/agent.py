from copy import deepcopy
import random
import time
import logging

logger = logging.Logger("MANCALA", level=logging.DEBUG)


class MancalaAgent:

    def __init__(self, player_side):
        self.player_side = player_side
        self.set_game()
        self.games = []

    def get_state_of_game(self, holes, scoreboard):
        tmp_state = []
        for player_idx in (self.player_side, not self.player_side):
            for hole in holes[player_idx]:
                tmp_state.append(hole.n_marbles)
            tmp_state.append(scoreboard[player_idx].n_marbles)
        # print(tmp_state)
        self.states.append(tmp_state)
        # print(f"PLAYER {self.player_side} STATES: {self.states}")

    def set_game(self):
        self.actions = []
        self.rewards = []
        self.states = []
        self.turns = []

    def store_game_results(self):
        tmp_game = {
            "actions": deepcopy(self.actions),
            "turns": deepcopy(self.turns),
            "rewards": deepcopy(self.rewards),
            "states": deepcopy(self.states),
            "results": sum(self.rewards)
        }

        self.games.append(tmp_game)
        self.set_game()

    def store_rewards(self, scoreboard):
        reward = scoreboard - sum(self.rewards)
        self.rewards.append(reward)
        # print(f"PLAYER {self.player_side} REWARDS: {self.rewards}")



class RandomAgent(MancalaAgent):

    def __init__(self, player_side):
        super().__init__(player_side)
        self.player_side = player_side

    def select_from_possible_holes(self, holes, time_delay=0):
        time.sleep(time_delay)
        return self.player_side, random.choice(holes)


class HumanAgent(MancalaAgent):

    def __init__(self, player_side):
        super().__init__(player_side)
        self.player_side = player_side
