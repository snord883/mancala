import tkinter as tk


class Hole:
    hole_label = None
    outer_board = None
    player_i = None
    hole_i = None
    opposite_hole_i = None
    n_marbles = 4

    def __init__(self, board, side_i, hole_i, outer_board):
        self.outer_board = outer_board
        self.player_i = side_i
        self.hole_i = hole_i
        self.opposite_hole_i = 5 - hole_i
        position_x = 0.15 + 0.12 * hole_i if side_i == 0 else 0.75 - 0.12 * hole_i
        self.hole_label = tk.Label(board, text=self.n_marbles, bg='#c87e4f')
        self.hole_label.place(relheight=0.2, relwidth=0.1, relx=position_x, rely=0.7 - side_i * .6)
        self.hole_label.bind('<Button-1>', self.hole_clicked)

    def reset(self):
        self.n_marbles = 4
        self.update_hole_label()

    def add_marbles(self, n=1):
        print(f'Add one to SIDE {self.player_i} & HOLE {self.hole_i}')
        self.n_marbles += n
        self.update_hole_label()

    def update_hole_label(self):
        self.hole_label['text'] = self.n_marbles

    def hole_clicked(self, other):
        if self.outer_board.player_up != self.player_i:
            print(f'Wrong side of the board for Player {str(self.outer_board.player_up)}')
        elif self.n_marbles == 0:
            print(f'Please select a hole on Player {str(self.outer_board.player_up)}\'s side with marbles in it.')
        else:
            self.outer_board.side_i = self.player_i
            self.outer_board.hole_i = self.hole_i + 1
            self.outer_board.marbles_in_hand = self.get_marbles()
            self.outer_board.currently_moving = True
            self.outer_board.move_marbles()

    def is_empty(self):
        return self.n_marbles == 0

    def get_marbles(self):
        print(f'From SIDE {self.player_i} & HOLE {self.hole_i}: {self.n_marbles} marbles grabbed')
        temp = self.n_marbles
        self.n_marbles = 0
        self.update_hole_label()
        return temp

    def get_opposite_hole(self):
        return self.outer_board.game_board[flip(self.player_i)][self.opposite_hole_i]


flip = lambda x: int(not x)
