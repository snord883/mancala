import tkinter as tk

class Hole():
    position_n = None
    marbles = 4

    def __init__(self, board, side_i, hole_i):
        self.position_n = side_i*10 + hole_i
        position_x = 0.15 + 0.12*hole_i if side_i==0 else 0.75 - 0.12*hole_i
        board = tk.Label(board, text=self.position_n, bg='#c87e4f')
        board.place(relheight=0.2,relwidth=0.1,relx=position_x,rely=0.7-side_i*.6)