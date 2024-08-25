from tkinter import *
import random

def next_turn(row, column):
    
    global player 

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player ==Players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = Players[1]
                label.config(text=( Players[1]+ "turn"))
            
            elif check_winner() is True:
                label.config(text = (Players[0]+" wins.."))
            
            elif check_winner() =="Tie":
                label.config(text = ("TIE!"))
            
        else:
            if player ==Players[1]:
                buttons[row][column]['text'] = player

            if check_winner() is False:
                player = Players[0]
                label.config(text=( Players[0]+ "turn"))
            
            elif check_winner() is True:
                label.config(text = (Players[1]+" wins.."))
            
            elif check_winner() =="Tie":
                label.config(text = ("TIE!"))
        
 
def check_winner():
    
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] !="":
            return True

    for i in range(3):
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] !="":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
        return True
    
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !="":
        return True

    elif empty_spaces is False:
        return "tie"

    else:
        return False
    
def empty_spaces():
    pass

def new_game():
    pass

window = Tk()
window.title ( "TIC-TAC-TOE")

Players=["X","0"]
player=random.choice(Players)
buttons=  [[0,0,0] 
           , [0,0,0],
             [0,0,0] ]
label = Label(text=player + " turn", font =('consolas',40))
label.pack(side="top")

reset_button = Button(text= "Restart", font =('consolas',20),command = new_game)
reset_button.pack(side="top")

frame= Frame(window)
frame.pack()

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame,text ="O",font=('consolas',20),width = 5,height=2, 
                              command = lambda row =i ,column = j : next_turn(row,column)  )
        buttons[i][j].grid(row= i , column = j)
window.mainloop()

