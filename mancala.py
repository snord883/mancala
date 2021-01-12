import tkinter as tk
from board import Board

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        board = Board(master=master)

root = tk.Tk()
app = Application(master=root)
root.title("MANCALA!!!")
root.geometry('600x300')
app.mainloop()