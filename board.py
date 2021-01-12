import tkinter as tk
import time

from store import Store

<<<<<<< Updated upstream
=======
speed_of_play = 10

>>>>>>> Stashed changes
class Board():
    master = None
    board = None
    player_up = 0
    scoreboard = None
    game_board = None
   
    def __init__(self,master):
        self.master = master
        self.board = tk.Frame(master, bg='#3d2606')
        self.board.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)
        self.scoreboard = [Store(self.board,store_i=i) for i in range(2)]
        self.game_board = [[self.Hole(board=self.board,side_i=j, hole_i=i, outer_board=self) for i in range(6)] for j in range(2)]
        self.rematch_prompt()
        
    def reset_board(self):
        _ = [self.scoreboard[i].reset() for i in range(2)]
        _ = [[self.game_board[j][i].reset() for i in range(6)] for j in range(2)]

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
            self.marbles_in_hand = 0
            self.currently_moving = False
            print('EXTRA TURN :)')
            self.is_game_over()
        else:
            self.switch_sides()

    def handle_last_marble_for_hole(self):
        if self.game_board[self.side_i][self.hole_i].is_empty():
            if self.side_i==self.player_up:
                opposite_hole_i = self.game_board[self.side_i][self.hole_i].get_opposite_hole()
                self.scoreboard[self.player_up].add_marbles(opposite_hole_i.get_marbles())
                self.scoreboard[self.player_up].add_marbles()
            else:
                self.game_board[self.side_i][self.hole_i].add_marbles()
            self.marbles_in_hand = 0
            self.turn_over()
        else:
            self.marbles_in_hand += self.game_board[self.side_i][self.hole_i].get_marbles()
            self.hole_i += 1

    def drop_marble_and_continue(self):
        if self.is_this_a_store():
            if self.side_i==self.player_up:
                print('score one for PLAYER {}: now has {} points and {} marbles remain in hand'.format(self.player_up,self.scoreboard[self.player_up],self.marbles_in_hand-1))
                self.score_and_switch()
            else:
                print('Skip this store: {} marbles remain in hand'.format(self.marbles_in_hand))
                self.switch_sides()
        else:
            print('Skip this store: {} marbles remain in hand'.format(n_marbles))

    def add_marble_to_hole(self):
        self.game_board[self.side_i][self.hole_i].add_marbles()
        self.hole_i += 1
        self.marbles_in_hand -= 1

    def score_and_switch(self):
        self.add_marble_to_store()
        self.switch_sides()

    def add_marble_to_store(self):
        self.scoreboard[self.player_up].add_marbles()
        self.marbles_in_hand -= 1

    def switch_sides(self):
        self.side_i = int(not self.side_i)
        self.hole_i = 0 
    
    def is_this_a_store(self):
        return self.hole_i == 6

    def turn_over(self):
        self.player_up = flip(self.player_up)
        self.currently_moving = False
        print("Turn over :(")
        self.is_game_over()
        
    def is_game_over(self):
        if self.sum_marbles_from_side(0) == 0 or self.sum_marbles_from_side(1) == 0:
            _ = [[self.scoreboard[i].add_marbles(self.game_board[i][j].get_marbles()) for i in range(2)] for j in range(6)]
            self.pick_winner()
            return True
        return False        

    def sum_marbles_from_side(self,n):
        print('{} marbles remain on side {}'.format(sum([self.game_board[n][i].n_marbles for i in range(6)]),n))
        return sum([self.game_board[n][i].n_marbles for i in range(6)])

    def pick_winner(self):
        if self.scoreboard[0]==self.scoreboard[1]:
            print('TIE GAME...TIEBREAKER...REMATCH!')
            return None
        else:
            winner = int(self.scoreboard[1].n_marbles > self.scoreboard[0].n_marbles)
            print('CONGRATULATIONS TO PLAYER {}'.format(winner))
            return winner

    def rematch_prompt(self):
        print('Prompt for rematch')
        frame = tk.Frame(self.master)
        frame.pack()

        rematch = tk.Button(frame,
                        text="REMATCH!",
                        command=self.reset_board)
        rematch.pack(side=tk.LEFT)


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

        def reset(self):
            self.n_marbles =4
            self.update_hole_label()

        def add_marbles(self,n=1):
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
            