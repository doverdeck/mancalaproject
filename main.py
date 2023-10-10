import tkinter as tk
from tkinter import *
# Create the main window
root = tk.Tk()
root.title("Mancala")
counter=0
b=0
c=0
# Create a function to handle button clicks
def button_click(b,c):
    global counter
    print(f"{c}")
    print(f"{b}")
    row=c
    col=b
    if ((row==1 and counter==1) or (row==0 and counter==0)):
        for i in range(grid[c][b]):
            grid[c][b]=grid[c][b]-1
            if(row==1):
                if(col+1>6):
                    col=6
                    row=0
                    grid[0][6]=grid[0][6]+1
                else:
                    grid[row][col+1]=grid[row][col+1]+1
                    col=col+1
            elif(row==0):
                if (col-1<0):
                    col = 0
                    row = 1
                    grid[1][0]=grid[1][0]+1
                else:
                    grid[row][col-1] = grid[row][col - 1]+1
                    col = col-1
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
def check_winner():
    sum=0
    for i in range(6):
        sum=sum+grid[0][i+1]
    sum2=0
    for j in range(6):
        sum2=sum2+grid[1][j]
    if(sum==0):
        grid[1][6]=sum2+grid[1][6]
        for j in range(6):
            grid[1][j]=0
        show_winner()
    elif(sum2==0):
        grid[0][0] = sum + grid[0][0]
        for i in range(6):
            grid[0][i + 1]=0
        show_winner()
def show_winner():
    if (grid[0][0] > grid[1][6]):
        main = tk.Tk()
        main.title("Player 1 Wins!")
        text = Label(main, text="PLAYER 1 WINS")
        text.grid(row=0, padx=10, pady=10)
    elif (grid[0][0] < grid[1][6]):
        main = tk.Tk()
        main.title("Player 2 Wins!")
        text = Label(main, text="PLAYER 2 WINS")
        text.grid(row=0, padx=10, pady=10)
    else:
        main = tk.Tk()
        main.title("Tie")
        text = Label(main, text="TIE")
        text.grid(row=0, padx=10, pady=10)

# Create a 2x7 grid of buttons
buttons = [[1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7]]
grid = [[0, 4, 4, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4, 0]]
for i in range(2):
    b=0
    for j in range(7):
        if ((i==0 and j==0)or(i==1 and j==6)):
            button = tk.Button(root, fg = 'brown' , width=10, height=12, text=f"{grid[c][b]}")
        else:
            button = tk.Button(root, width=10, height=4, text=f"{grid[c][b]}", command=lambda b=b, c=c: button_click(b, c))
        b=b+1
        print(f"{b}")
        button.grid(row=i, column=j)
        if (i==0):
            button.place(x=j*80,y=20)
        if (i==1):
            button.place(x=80+j*80,y=100)
        if(i==0 and j==0):
            button.place(x=0, y=0)
        if (i == 1 and j == 6):
            button.place(x=80 + j * 80, y=0)
        buttons[i][j] = button
    c = c + 1
# Start the tkinter main loop
root.mainloop()