import tkinter as tk

DISABLED_HOLE_COLOR = '#111111'
ENABLED_HOLE_COLOR = '#c87e4f'

class Hole:
    hole_label = None
    side_i = None
    hole_i = None
    n_marbles = 4

    def __init__(self, side_i, hole_i, frame=None, enabled=False):
        self.side_i = side_i
        self.hole_i = hole_i
        position_x = 0.15 + 0.12 * hole_i if side_i == 0 else 0.75 - 0.12 * hole_i
        self.hole_label = tk.Label(frame, text=self.n_marbles, bg=self.get_hole_color(enabled))
        self.hole_label.place(relheight=0.2, relwidth=0.1, relx=position_x, rely=0.7 - self.side_i * .6)

    def get_hole_color(self, enabled):
        return ENABLED_HOLE_COLOR if enabled and self.n_marbles>0 else DISABLED_HOLE_COLOR

    def reset(self):
        self.n_marbles = 4
        self.update_hole_label()

    def add_marbles(self, n=1):
        print(f'Add {n} to SIDE {self.side_i} & HOLE {self.hole_i}')
        self.n_marbles += n
        self.update_hole_label()

    def update_hole_label(self):
        if self.hole_label is not None:
            self.hole_label['text'] = self.n_marbles

    def update_hole_color(self, enabled=False):
        self.hole_label['bg'] = self.get_hole_color(enabled)

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
