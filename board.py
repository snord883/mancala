import tkinter as tk
import time

from store import Store

class Board():
    master = None
    player_up = 0
    scoreboard = None
    game_board = None
   
    def __init__(self,master):
        self.master = master
        self.board = tk.Frame(master, bg='#3d2606')
        self.board.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)
        
        self.scoreboard = [Store(self.board,store_i=i) for i in range(2)]
        self.game_board = [[self.Hole(board=self.board,side_i=j, hole_i=i, outer_board=self) for i in range(6)] for j in range(2)]

    def move_marbles(self,side_i,hole_i,n_marbles):
        if n_marbles==0:
            if hole_i == 6:
                print("EXTRA TURN!!")
                return None
            elif not self.game_board[side_i][hole_i].get_marbles():
                if side_i==self.player_up:
                    self.scoreboard[self.player_up].add_marbles(self.game_board[int(not self.player_up)][5-hole_i])

        hole_i += 1
        if hole_i == 6:
            side_i, hole_i, n_marbles = self.reached_store(side_i,n_marbles)
        else:
            self.game_board[side_i][hole_i].add_marble()
            n_marbles -= 1
        self.master.after(1500, self.move_marbles,side_i,hole_i,n_marbles)

    def reached_store(self,side_i,n_marbles):
        hole_i = -1
        if side_i == self.player_up:
            print('score one for PLAYER {}: {} marbles remain in hand'.format(side_i,n_marbles-1))
            self.scoreboard[self.player_up].add_marbles()
            n_marbles -= 1
            hole_i= hole_i if n_marbles is not 0 else 6
        else:
            print('Skip this store: {} marbles remain in hand'.format(n_marbles))

        print('Exit from store: heading to SIDE {} HOLE {} with {} MARBLES'.format(int(not side_i),hole_i,n_marbles))
            
        return [not side_i, hole_i, n_marbles]
        
        


    class Hole():
        hole_label = None
        outer_board = None
        player_i = None
        hole_i = None
        n_marbles = 4

        def __init__(self, board, side_i, hole_i, outer_board):
            self.outer_board = outer_board
            self.player_i = side_i
            self.hole_i = hole_i
            position_x = 0.15 + 0.12*hole_i if side_i==0 else 0.75 - 0.12*hole_i
            self.hole_label = tk.Label(board, text=self.n_marbles, bg='#c87e4f')
            self.hole_label.place(relheight=0.2,relwidth=0.1,relx=position_x,rely=0.7-side_i*.6)
            self.hole_label.bind('<Button-1>',self.hole_clicked)

        def add_marble(self,n=1):
            print('Add one to SIDE {} & HOLE {}'.format(self.player_i,self.hole_i))
            self.n_marbles += n
            self.update_hole_label()

        def update_hole_label(self):
            self.hole_label['text'] = self.n_marbles

        def hole_clicked(self, other):
            if self.outer_board.player_up!=self.player_i:
                print('Wrong side of the board for Player', str(self.outer_board.player_up+1))
            elif self.n_marbles==0:
                print('Please select a hole on Player {}\'s side with marbles in it.'.format(str(self.outer_board.player_up+1)))
            else:
                self.get_marbles()

        def get_marbles(self):
            if self.n_marbles == 0:
                print('From SIDE {} & HOLE {}: NO marbles grabbed!!'.format(self.player_i,self.hole_i))
                self.n_marbles = 1
                self.update_hole_label()
                return False
            else:
                print('From SIDE {} & HOLE {}: {} marbles grabbed'.format(self.player_i,self.hole_i,self.n_marbles))
                temp = self.n_marbles
                self.n_marbles = 0
                self.update_hole_label()
                self.outer_board.move_marbles(self.player_i,self.hole_i,temp)
            