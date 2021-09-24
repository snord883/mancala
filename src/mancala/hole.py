import tkinter as tk
import logging

DISABLED_BACKGROUND_COLOR = '#101010'
ENABLED_BACKGROUND_COLOR = '#c87e4f'
WHITE_FONT_COLOR = "white"
BLACK_FONT_COLOR = "black"

logger = logging.Logger("MANCALA", level=logging.DEBUG)


class Hole:
    hole_label = None
    side_i = None
    hole_i = None
    n_marbles = 4
    enabled = False

    def __init__(self, side_i, hole_i, enabled):
        self.side_i = side_i
        self.hole_i = hole_i
        self.enabled = enabled

    def display(self, frame):
        position_x = 0.15 + 0.12 * self.hole_i if self.side_i == 0 else 0.75 - 0.12 * self.hole_i
        self.hole_label = tk.Label(
                                frame,
                                text=self.n_marbles,
                                bg=self.get_background_color(),
                                fg=self.get_font_color())
        self.hole_label.place(relheight=0.2, relwidth=0.1, relx=position_x, rely=0.7 - self.side_i * .6)

    def get_background_color(self):
        return ENABLED_BACKGROUND_COLOR if self.enabled and not self.is_empty() else DISABLED_BACKGROUND_COLOR

    def get_font_color(self):
        return WHITE_FONT_COLOR if not self.enabled and not self.is_empty() else BLACK_FONT_COLOR

    def reset(self, enabled):
        self.n_marbles = 4
        self.enabled = enabled
        self.update_hole_label()
        self.update_hole_color()

    def add_marbles(self, n=1):
        print(f'Add {n} to SIDE {self.side_i} & HOLE {self.hole_i}')
        self.n_marbles += n
        self.update_hole_label()

    def update_hole_label(self):
        if self.hole_label is not None:
            self.hole_label['text'] = self.n_marbles

    def update_hole_color(self):
        self.hole_label['bg'] = self.get_background_color()
        self.hole_label['fg'] = self.get_font_color()

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
