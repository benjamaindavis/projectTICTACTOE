from tkinter import *
import random
import game_logic

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

game_logic = game_logic.Logic() # im being extra and made it a package for neatness

window = Tk() # instantiates a window (doesnt open it)
window.geometry('600x600')
window.title('Tic-Tac_Toe')

players = ['x turn', 'o turn']
player = random.choice(players)
grid = [[0,0,0], 
        [0,0,0], 
        [0,0,0]]

label = Label(window, text=f'{player}\'s turn', font=('Arial', 20))
label.pack(side = TOP) # label location

icon = PhotoImage(file='tictactoe.png')
window.iconphoto(True, icon)
window.config(bg='teal') # can be replaced with hex color codes
reset_button = Button(text = 'restart', font=('Arial', 10), command = game_logic.new_game)
reset_button.pack(side = TOP)

window.mainloop() # opens a new window!