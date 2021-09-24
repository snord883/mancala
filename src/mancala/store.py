import tkinter as tk


class Store:
    store_label = None
    store_i = None
    n_marbles = 0

    def __init__(self, store_i):
        self.store_i = store_i

    def display(self, frame):
        self.store_label = tk.Label(frame, text=self.n_marbles, bg='#c87e4f')
        self.store_label.place(relheight=0.8, relwidth=0.11, relx=0.87 - 0.85 * self.store_i, rely=0.1)

    def add_marbles(self, n=1):
        self.n_marbles += n
        self.update_store_label()

    def update_store_label(self):
        if self.store_label is not None:
            self.store_label['text'] = self.n_marbles

    def reset(self):
        self.n_marbles = 0
        self.update_store_label()
