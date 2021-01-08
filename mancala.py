import tkinter as tk
from hole import Hole
from store import Store

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_board()

    def create_board(self):
        self.board = tk.Frame(self.master, bg='#3d2606')
        self.board.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)
        
        scoreboard = [Store(self.board,store_i=i) for i in range(2)]
        game_board = [[Hole(self.board,side_i=j, hole_i=i) for i in range(6)] for j in range(2)]
        print('Rows: ',len(game_board))
        print('Columns: ',len(game_board[0]))
        # def hole_picked()

root = tk.Tk()
app = Application(master=root)
root.title("MANCALA!!!")
root.geometry('1200x600')
app.mainloop()