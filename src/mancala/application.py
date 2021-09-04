import tkinter as tk
from game import Game
from agent import HumanAgent, RandomAgent

games_played = 0


class Application(tk.Frame):
    # game =

    def play(self, master=None):
        self.pack()
        player0 = HumanAgent(0)
        player1 = HumanAgent(1)
        game = Game(players=[player0, player1], master=master)
        print("NORD")

    # def simulate(self):

# def


root = tk.Tk()
app = Application()
app.play(master=root)
root.title("MANCALA!!!")
root.geometry('600x300')
app.mainloop()
