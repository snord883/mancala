import tkinter as tk
from board import Board


class Application(tk.Frame):

    def play(self, master=None):
        self.pack()
        board = Board(master=master)

    # def simulate(self):


root = tk.Tk()
app = Application()
app.play(master=root)
root.title("MANCALA!!!")
root.geometry('600x300')
app.mainloop()
