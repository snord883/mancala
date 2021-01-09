import tkinter as tk

class Store():
    store_label = None
    position_n = None
    n_marbles = 0

    def __init__(self, board, store_i):
        self.position_n = store_i
        self.store_label = tk.Label(board, text=self.n_marbles, bg='#c87e4f')
        self.store_label.place(relheight=0.8,relwidth=0.11,relx=0.87 - 0.85*store_i,rely=0.1)

    def add_marbles(self, n=1):
        self.n_marbles += n
        self.store_label['text'] = self.n_marbles