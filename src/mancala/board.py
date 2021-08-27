import tkinter as tk
from store import Store
from hole import Hole, flip

speed_of_play = 10


class Board:
    master = None
    board = None
    player_up = 0
    side_i = None
    hole_i = None
    currently_moving = False
    marbles_in_hand = 0
    scoreboard = None
    game_board = None

    def __init__(self, master):
        self.master = master
        self.board = tk.Frame(master, bg='#3d2606')
        self.board.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
        self.scoreboard = [Store(self.board, store_i=i) for i in range(2)]
        self.game_board = [[Hole(board=self.board, side_i=j, hole_i=i, outer_board=self) for i in range(6)] for j
                           in range(2)]
        self.rematch_prompt()

    def reset_board(self):
        self.player_up = 0
        _ = [self.scoreboard[i].reset() for i in range(2)]
        _ = [[self.game_board[j][i].reset() for i in range(6)] for j in range(2)]

    def move_marbles(self):
        if self.marbles_in_hand == 1:
            self.handle_last_marble()
        else:
            self.drop_marble_and_continue()

        if self.currently_moving:
            self.master.after(speed_of_play, self.move_marbles)
        else:
            return None

    def handle_last_marble(self):
        if self.is_this_a_store():
            self.handle_last_marble_for_store()
        else:
            self.handle_last_marble_for_hole()

    def handle_last_marble_for_store(self):
        if self.side_i == self.player_up:
            self.scoreboard[self.player_up].add_marbles()
            self.marbles_in_hand = 0
            self.currently_moving = False
            print('EXTRA TURN :)')
            self.is_game_over()
        else:
            self.switch_sides()

    def handle_last_marble_for_hole(self):
        if self.game_board[self.side_i][self.hole_i].is_empty():
            if self.side_i == self.player_up:
                opposite_hole_i = self.game_board[self.side_i][self.hole_i].get_opposite_hole()
                self.scoreboard[self.player_up].add_marbles(opposite_hole_i.get_marbles())
                self.scoreboard[self.player_up].add_marbles()
            else:
                self.game_board[self.side_i][self.hole_i].add_marbles()
            self.marbles_in_hand = 0
            self.turn_over()
        else:
            self.marbles_in_hand += self.game_board[self.side_i][self.hole_i].get_marbles()
            self.hole_i += 1

    def drop_marble_and_continue(self):
        if self.is_this_a_store():
            if self.side_i == self.player_up:
                print(
                    f'score one for PLAYER {self.player_up}: now has {self.scoreboard[self.player_up]} points and {self.marbles_in_hand - 1} marbles remain in hand')
                self.score_and_switch()
            else:
                print(f'Skip this store: {self.marbles_in_hand} marbles remain in hand')
                self.switch_sides()
        else:
            self.add_marble_to_hole()

    def add_marble_to_hole(self):
        self.game_board[self.side_i][self.hole_i].add_marbles()
        self.hole_i += 1
        self.marbles_in_hand -= 1

    def score_and_switch(self):
        self.add_marble_to_store()
        self.switch_sides()

    def add_marble_to_store(self):
        self.scoreboard[self.player_up].add_marbles()
        self.marbles_in_hand -= 1

    def switch_sides(self):
        self.side_i = int(not self.side_i)
        self.hole_i = 0

    def is_this_a_store(self):
        return self.hole_i == 6

    def turn_over(self):
        self.player_up = flip(self.player_up)
        self.currently_moving = False
        print("Turn over :(")
        self.is_game_over()

    def is_game_over(self):
        if self.sum_marbles_from_side(0) == 0 or self.sum_marbles_from_side(1) == 0:
            _ = [[self.scoreboard[i].add_marbles(self.game_board[i][j].get_marbles()) for i in range(2)] for j in
                 range(6)]
            self.pick_winner()
            return True
        return False

    def sum_marbles_from_side(self, n):
        print(f'{sum([self.game_board[n][i].n_marbles for i in range(6)])} marbles remain on side {n}')
        return sum([self.game_board[n][i].n_marbles for i in range(6)])

    def pick_winner(self):
        if self.scoreboard[0] == self.scoreboard[1]:
            print('TIE GAME...TIEBREAKER...REMATCH!')
            return None
        else:
            winner = int(self.scoreboard[1].n_marbles > self.scoreboard[0].n_marbles)
            print(f'CONGRATULATIONS TO PLAYER {winner}')
            return winner

    def rematch_prompt(self):
        print('Prompt for rematch')
        frame = tk.Frame(self.master)
        frame.pack()

        rematch = tk.Button(frame,
                            text="REMATCH!",
                            command=self.reset_board)
        rematch.pack(side=tk.LEFT)