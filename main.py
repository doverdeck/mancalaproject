import tkinter as tk
from tkinter import *

# Create the main window
root = tk.Tk()
root.title("Mancala")
counter=0 # determines whose turn it is
b=0 #b is the y-cord
c=0 #c is the x-cord
# Create a function to handle button clicks
def button_click(b,c): # whenever a button is pressed
    global counter
    print(f"{c}")
    print(f"{b}")
    row=c
    col=b
    if ((row==1 and counter==1) or (row==0 and counter==0)): #counter 1 is player 2 - 0 is player 1
        #ensures that player 1 cannot click buttons in the bottm row - vice versa for player 2
        for i in range(grid[c][b]): # traverse the grid
            grid[c][b]=grid[c][b]-1 # remove a token
            if(row==1):# if it is bottom row
                if(col+1>6): # and I clicked on the mancala
                    col=6 # move to the 6th colum
                    row=0 # in the top row
                    grid[0][6]=grid[0][6]+1 # then add a token
                else: # if its any other button
                    grid[row][col+1]=grid[row][col+1]+1 # add a token to the next col
                    col=col+1 # move one to the right
            elif(row==0): # if it is the top row
                if (col-1<0): # and I click on the Mancala
                    col = 0
                    row = 1
                    grid[1][0]=grid[1][0]+1
                else: # if it's any other button in top row
                    grid[row][col-1] = grid[row][col - 1]+1 # add a token
                    col = col-1 # move one button to the left
        if (counter==0 and (col!=0 or row!=0)):
            counter=1
        elif(counter==1 and (col!=6 or row!=1)):
            counter=0

    print(f"grid={grid[c][b]}")
    check_winner()
    update_text()
def update_text():
    for i in range(2):
        for j in range(7):
            buttons[i][j].config(text=f"{grid[i][j]}")
def check_winner(): # this method checks to see if there is a winner
    sum=0
    for i in range(6): # sums up all the tokens in the top row
        sum=sum+grid[0][i+1]
    sum2=0
    for j in range(6): # sums up all the tokens in the bottom rown
        sum2=sum2+grid[1][j]
    if(sum==0):# if there are no remaining tokens in top row
        grid[1][6]=sum2+grid[1][6] # then move all player 2 remaining tokens into their mancala
        for j in range(6): # reset all the pits to 0
            grid[1][j]=0
        show_winner() # show that the winner won
    elif(sum2==0):# if there are no remaing tokens in bottom row
        grid[0][0] = sum + grid[0][0] # bring all the tokens from the row into player 1 mancala
        for i in range(6): # reset all the pits to 0
            grid[0][i + 1]=0
        show_winner() # show that winner won
def show_winner(): # method to show the winner
    if (grid[0][0] > grid[1][6]): # if player 1 mancala value is larger than player 2
        main = tk.Tk()
        main.title("Player 1 Wins!")
        text = Label(main, text="PLAYER 1 WINS")
        text.grid(row=0, padx=10, pady=10)
    elif (grid[0][0] < grid[1][6]): # vice versa - player 2 wins
        main = tk.Tk()
        main.title("Player 2 Wins!")
        text = Label(main, text="PLAYER 2 WINS")
        text.grid(row=0, padx=10, pady=10)
    else: # if there is a tie
        main = tk.Tk()
        main.title("Tie")
        text = Label(main, text="TIE")
        text.grid(row=0, padx=10, pady=10)
def check_steal():
    p1_final_index = c - grid[c,b]
    p2_final_index = c + grid[c,b]
    #if p2_final_index> 5:
    if counter == 0:
        print(grid[p1_final_index,counter])
        if grid[p1_final_index,counter] == 0:
            grid[p1_final_index,counter] = grid[p2_final_index,1]
            grid[p2_final_index,1] = 0
    else:
        if grid[p2_final_index, counter] == 0:
            grid[p2_final_index, counter] = grid[p1_final_index,1]
            grid[p1_final_index,1] = 0

# Create a 2x7 grid of buttons
buttons = [[1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7]]
grid = [[0, 4, 4, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4, 0]]

for i in range(2): #2 by 7 array rows
    b=0
    for j in range(7): # columns
        if ((i==0 and j==0)or(i==1 and j==6)): # if the button is a mancala pit
            button = tk.Button(root, fg = 'brown' , width=10, height=12, text=f"{grid[c][b]}")
        else: # if it isnt a mancala pit
            button = tk.Button(root, width=10, height=4, text=f"{grid[c][b]}", command=lambda b=b, c=c: button_click(b, c))
        b=b+1
        print(f"{b}")
        button.grid(row=i, column=j)
        if (i==0): # placement for all the top rows of buttons
            button.place(x=j*80,y=20)
        if (i==1): # placement for all the bottom rows of buttons
            button.place(x=80+j*80,y=100)
        if(i==0 and j==0): # placement for player 1 mancala pit
            button.place(x=0, y=0)
        if (i == 1 and j == 6): # placement for player 2 mancala
            button.place(x=80 + j * 80, y=0)
        buttons[i][j] = button
    c = c + 1
# Start the tkinter main loop
root.mainloop()