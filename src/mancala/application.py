import tkinter as tk
from game import Game
from agent import HumanAgent, RandomAgent


class Application(tk.Frame):

    def play(self, master=None):
        self.pack()
        player0 = HumanAgent(0)
        player1 = HumanAgent(1)
        board = Game(players=[player0,player1], master=master)

    # def simulate(self):


root = tk.Tk()
app = Application()
app.play(master=root)
root.title("MANCALA!!!")
root.geometry('600x300')
app.mainloop()
