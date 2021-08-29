import tkinter as tk


class Hole:
    hole_label = None
    outer_board = None
    side_i = None
    hole_i = None
    n_marbles = 4

    def __init__(self, frame, side_i, hole_i, outer_board):
        self.outer_board = outer_board
        self.side_i = side_i
        self.hole_i = hole_i
        position_x = 0.15 + 0.12 * hole_i if side_i == 0 else 0.75 - 0.12 * hole_i
        self.hole_label = tk.Label(frame, text=self.n_marbles, bg='#c87e4f')
        self.hole_label.place(relheight=0.2, relwidth=0.1, relx=position_x, rely=0.7 - side_i * .6)
        self.hole_label.bind('<Button-1>', self.hole_clicked)

    def reset(self):
        self.n_marbles = 4
        self.update_hole_label()

    def add_marbles(self, n=1):
        print(f'Add {n} to SIDE {self.side_i} & HOLE {self.hole_i}')
        self.n_marbles += n
        self.update_hole_label()

    def update_hole_label(self):
        self.hole_label['text'] = self.n_marbles

    def hole_clicked(self, other):
        self.outer_board.hole_selected(self.side_i, self.hole_i)

    def is_empty(self):
        return self.n_marbles == 0

    def grab_marbles(self):
        print(f'From SIDE {self.side_i} & HOLE {self.hole_i}: {self.n_marbles} marbles grabbed')
        temp = self.n_marbles
        self.n_marbles = 0
        self.update_hole_label()
        return temp

    def get_n_marbles(self):
        return self.n_marbles
