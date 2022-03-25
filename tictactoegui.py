from tkinter import *
import tkinter.font as font

def disable_event():
    pass

class TicTacToe:
    board = [' ' for i in range(10)]
    p1 = 'X'
    p2 = 'O'
    
    def game(self):
        self.player1 = True
        self.board = [' ' for i in range(10)]
        win = Tk()
        win.title("TicTacToe Board")
        win.configure(bg = "#000000")
        self.createButtons(win)
        win.resizable(False, False)
        win.mainloop()
        
        
    def victory(self):
        if self.board[7] == self.board[8] == self.board[9] != ' ':
            return 1
        if self.board[4] == self.board[5] == self.board[6] != ' ':
            return 1
        if self.board[1] == self.board[2] == self.board[3] != ' ':
            return 1
        if self.board[7] == self.board[4] == self.board[1] != ' ':
            return 1
        if self.board[8] == self.board[5] == self.board[2] != ' ':
            return 1
        if self.board[9] == self.board[6] == self.board[3] != ' ':
            return 1
        if self.board[7] == self.board[5] == self.board[3] != ' ':
            return 1
        if self.board[9] == self.board[5] == self.board[1] != ' ':
            return 1
        if ' ' not in self.board[1: ]:
            return 2
        return 0
    
    def createButtons(self, win):
        S7 = Button(win, text = self.board[7], width = 20, height = 10, borderwidth = 3, relief = 'ridge', background = '#e0e0eb', activebackground = '#d1d1e0', command = lambda: obj.onClick(7, S7, win))
        S7.grid(row = 0, column = 0)
        S8 = Button(win, text = self.board[8], width = 20, height = 10, borderwidth = 3, relief = 'ridge', background = '#e0e0eb', activebackground = '#d1d1e0', command = lambda: obj.onClick(8, S8, win))
        S8.grid(row = 0, column = 1)
        S9 = Button(win, text = self.board[9], width = 20, height = 10, borderwidth = 3, relief = 'ridge', background = '#e0e0eb', activebackground = '#d1d1e0', command = lambda: obj.onClick(9, S9, win))
        S9.grid(row = 0, column = 2)
        S4 = Button(win, text = self.board[4], width = 20, height = 10, borderwidth = 3, relief = 'ridge', background = '#e0e0eb', activebackground = '#d1d1e0', command = lambda: obj.onClick(4, S4, win))
        S4.grid(row = 1, column = 0)
        S5 = Button(win, text = self.board[5], width = 20, height = 10, borderwidth = 3, relief = 'ridge', background = '#e0e0eb', activebackground = '#d1d1e0', command = lambda: obj.onClick(5, S5, win))
        S5.grid(row = 1, column = 1)
        S6 = Button(win, text = self.board[6], width = 20, height = 10, borderwidth = 3, relief = 'ridge', background = '#e0e0eb', activebackground = '#d1d1e0', command = lambda: obj.onClick(6, S6, win))
        S6.grid(row = 1, column = 2)
        S1 = Button(win, text = self.board[1], width = 20, height = 10, borderwidth = 3, relief = 'ridge', background = '#e0e0eb', activebackground = '#d1d1e0', command = lambda: obj.onClick(1, S1, win))
        S1.grid(row = 2, column = 0)
        S2 = Button(win, text = self.board[2], width = 20, height = 10, borderwidth = 3, relief = 'ridge', background = '#e0e0eb', activebackground = '#d1d1e0', command = lambda: obj.onClick(2, S2, win))
        S2.grid(row = 2, column = 1)
        S3 = Button(win, text = self.board[3], width = 20, height = 10, borderwidth = 3, relief = 'ridge', background = '#e0e0eb', activebackground = '#d1d1e0', command = lambda: obj.onClick(3, S3, win))
        S3.grid(row = 2, column = 2)
    
    def result(self, p1, vict, win):
        if vict == 1:
            res = 'Player 1 wins!!' if p1 else 'Player 2 wins!!'
            bg = '#ff9999' if p1 else '#99ccff'
        elif vict == 2:
            res = 'Match draw!'
            bg = '#99ffcc'
            
        res_win = Toplevel(bg = bg)
        res_win.geometry("550x150")
        res_win.title("Result")
        Label(res_win, text = res, font = ('Mistral 18 bold'), bg = bg).place(x = 200, y = 60)
        ok = Button(res_win, text = 'Okay', height = 1, width = 4, relief = 'ridge', fg = '#ffffff', background = '#000000', activebackground = '#e60000', command = win.destroy)
        ok.place(x = 250, y = 110)
        res_win.protocol("WM_DELETE_WINDOW", disable_event)
        res_win.resizable(False, False)
        res_win.grab_set()
    
    def onClick(self, pos, button, win):
        self.board[pos] = self.p1 if self.player1 else self.p2
        button['text'] = self.board[pos]
        button['background'] = '#99ccff' if self.board[pos] == 'O' else '#ff9999'
        button['state'] = 'disabled'
        vict = self.victory()
        if vict == 1 or vict == 2:
            self.result(self.player1, vict, win)
        self.player1 = not self.player1

obj = TicTacToe()
def yClick(win):
    win.destroy()
def nClick(win):
    global flag
    flag = 0
    win.destroy()

flag = 1
while flag:
    obj.game()
    choice = Tk()
    choice.geometry('350x175')
    choice.title("Choice")
    choice.configure(bg = '#000000')
    Label(choice, text = "Do you want to play again?", fg = '#ffff00', bg = '#000000', font = ('Mistral 18 bold')).pack(pady = 30)
    yes = Button(choice, text = 'Yes', command = lambda: yClick(choice), height = 1, width = 5, bg = "#33cc33")
    yes.pack(padx = 0, pady = 0)
    no = Button(choice, text = 'No', command = lambda: nClick(choice), height = 1, width = 5, bg = "#ff0000")
    no.pack(padx = 0, pady = 0)
    choice.protocol("WM_DELETE_WINDOW", disable_event)
    choice.resizable(False, False)
    choice.mainloop()