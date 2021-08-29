

class MancalaAgent:
    possible_states = []

    def __init__(self, player_side):
        self.player_side = player_side



class RandomAgent(MancalaAgent):

    def __init__(self, player_side):
        super(RandomAgent, self).__init__(player_side)


class HumanAgent(MancalaAgent):

    def __init__(self, player_side):
        super(HumanAgent, self).__init__(player_side)
