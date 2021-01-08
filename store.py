import tkinter as tk

class Store():
    marbles = 0

    def __init__(self, board, store_i):
        board = tk.Label(board, text=store_i, bg='#c87e4f')
        board.place(relheight=0.8,relwidth=0.11,relx=0.87 - 0.85*store_i,rely=0.1)

    def add_marble(self):
        self.marbles += 1