import tkinter as tk
from game import Simulation, AnimatedGame
from agent import HumanAgent, RandomAgent


class Application(tk.Frame):
    game = None

    def play(self, master=None):
        self.pack()
        self.game = AnimatedGame(players=[HumanAgent(0), HumanAgent(1)], master=master)

    def simulate(self):
        self.game = Simulation(n_games=10)

# def play_another():
#     app.game


root = tk.Tk()
app = Application()
# app.play(master=root)
# root.title("MANCALA!!!")
# root.geometry('600x300')
# app.mainloop()

app.simulate()
