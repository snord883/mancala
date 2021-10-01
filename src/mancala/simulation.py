import json
from tqdm import tqdm
from agent import RandomAgent
from copy import deepcopy

SIDE_HOLES = [4, 4, 4, 4, 4, 4]

agents = [RandomAgent(0), RandomAgent(1)]

STARTING_STATE = {
    "board": SIDE_HOLES + [0] + SIDE_HOLES + [0],
    "player_up": 0,
    "turn_num": 0
}

CURRENT = "CURRENT"
OPPONENT = "OPPONENT"

CURRENT_STATE = None


def simulate_game():
    global CURRENT_STATE
    CURRENT_STATE = deepcopy(STARTING_STATE)
    while not is_game_over():
        action = select_action()
        if action is not None:
            play_turn(action)
            CURRENT_STATE["turn_num"] += 1

    get_final_results()
    for i in range(len(agents)):
        agents[i].store_game_results()


def select_action():
    global CURRENT_STATE
    agent = agents[CURRENT_STATE["player_up"]]
    agent.states.append(deepcopy(CURRENT_STATE["board"]))
    possible_holes = get_possible_holes()
    if possible_holes:
        _, action = agent.select_from_possible_holes(possible_holes)
        # ############
        # Used for replaying a specific game
        # actions_take = [
        #     [1, 5, 2, 5, 4, 3, 1, 1, 5, 1, 4, 5],
        #     [2, 5, 1, 4, 5, 4, 1, 5, 2]
        # ]
        # player_up = int(CURRENT_STATE["player_up"])
        # action = actions_take[player_up][len(agents[player_up].actions)]
        #
        # ########
        agent.actions.append(action)
        agent.turns.append(CURRENT_STATE["turn_num"])
        return action
    else:
        return None


def play_turn(hole_i):
    marbles_in_hand = grab_marbles_from_hole(hole_i)
    hole_i = move_to_next_spot_on_board(hole_i)
    while marbles_in_hand > 0:
        hole_i = place_marbles_in_appropriate_holes_stores_starting_at(hole_i, marbles_in_hand-1)
        hole_i, marbles_in_hand = handle_last_marble(hole_i)
    return hole_i


def handle_last_marble(hole_i):
    if is_this_hole_a_store(hole_i):
        return handle_last_marble_for_store(hole_i)
    else:
        return handle_last_marble_for_hole(hole_i)


def handle_last_marble_for_store(hole_i):
    global CURRENT_STATE
    if hole_i == get_store_idx_for_player(CURRENT):
        CURRENT_STATE["board"][hole_i] += 1
        hole_i, marbles = play_extra_turn()
        return hole_i, marbles
    else:
        hole_i = move_to_next_spot_on_board(hole_i)
        return handle_last_marble_for_hole(hole_i)


def handle_last_marble_for_hole(hole_i):
    global CURRENT_STATE
    if CURRENT_STATE["board"][hole_i] == 0:
        if is_this_hole_on_current_players_side(hole_i):
            marbles_from_opposite_hole = grab_marbles_from_opposite_hole(hole_i)
            CURRENT_STATE["board"][get_store_idx_for_player(CURRENT)] += marbles_from_opposite_hole + 1
        else:
            CURRENT_STATE["board"][hole_i] += 1
        flip_state()
        return hole_i, 0
    else:
        marbles = CURRENT_STATE["board"][hole_i] + 1
        CURRENT_STATE["board"][hole_i] = 0
        return move_to_next_spot_on_board(hole_i), marbles


def play_extra_turn():
    if is_game_over():
        return 0, 0
    hole_i = select_action()
    marbles = grab_marbles_from_hole(hole_i)
    player_up = CURRENT_STATE["player_up"]
    agents[player_up].store_rewards(CURRENT_STATE["board"][get_store_idx_for_player(CURRENT)])
    return move_to_next_spot_on_board(hole_i), marbles


def grab_marbles_from_hole(hole_i):
    global CURRENT_STATE
    marbles = CURRENT_STATE["board"][hole_i]*1
    CURRENT_STATE["board"][hole_i] = 0
    return marbles


def grab_marbles_from_opposite_hole(hole_i):
    global CURRENT_STATE
    opposite_hole_i = len(CURRENT_STATE["board"]) - hole_i - 1 - 1
    marbles = CURRENT_STATE["board"][opposite_hole_i] * 1
    CURRENT_STATE["board"][opposite_hole_i] = 0
    return marbles


def place_marbles_in_appropriate_holes_stores_starting_at(hole_i, n_marbles):
    global CURRENT_STATE
    for _ in range(n_marbles):
        if hole_i == get_store_idx_for_player(OPPONENT):
            hole_i = move_to_next_spot_on_board(hole_i)
        CURRENT_STATE["board"][hole_i] += 1
        hole_i = move_to_next_spot_on_board(hole_i)

    return hole_i


def move_to_next_spot_on_board(hole_i):
    return (hole_i + 1) % len(CURRENT_STATE["board"])


def is_this_hole_on_current_players_side(hole_i):
    return hole_i < len(SIDE_HOLES)


def is_this_hole_a_store(i):
    return i == get_store_idx_for_player(CURRENT) or i == get_store_idx_for_player(OPPONENT)


def get_store_idx_for_player(player):
    if player == CURRENT:
        return len(SIDE_HOLES)
    else:
        return len(STARTING_STATE["board"])-1


def get_possible_holes():
    global CURRENT_STATE
    player_ups_side = CURRENT_STATE["board"][0:len(SIDE_HOLES)]
    return [i for i, value in enumerate(player_ups_side) if value > 0]


def is_game_over():
    global CURRENT_STATE
    if sum(CURRENT_STATE["board"][:len(SIDE_HOLES)]) == 0 or sum(CURRENT_STATE["board"][len(SIDE_HOLES)+1:-1]) == 0:
        return True
    return False


def get_final_results():
    CURRENT_STATE["board"][len(SIDE_HOLES)] += sum(CURRENT_STATE["board"][:len(SIDE_HOLES)])
    agents[CURRENT_STATE["player_up"]].store_rewards(CURRENT_STATE["board"][len(SIDE_HOLES)])
    CURRENT_STATE["board"][-1] += sum(CURRENT_STATE["board"][len(SIDE_HOLES)+1:-1])
    agents[int(not CURRENT_STATE["player_up"])].store_rewards(CURRENT_STATE["board"][-1])


def flip_state():
    global CURRENT_STATE
    agents[CURRENT_STATE["player_up"]].store_rewards(CURRENT_STATE["board"][len(SIDE_HOLES)])
    CURRENT_STATE["board"] = CURRENT_STATE["board"][len(SIDE_HOLES)+1:] + CURRENT_STATE["board"][:len(SIDE_HOLES)+1]
    CURRENT_STATE["player_up"] = int(not CURRENT_STATE["player_up"])


for _ in tqdm(range(10000)):
    simulate_game()

z = {
    "0": agents[0].games,
    "1": agents[1].games,
}

with open("unprocessed_games.json", "w") as f:
    json.dump(z, f)

