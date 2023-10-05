import tkinter as tk
from tkinter import *
# Create the main window
root = tk.Tk()
root.title("Tic tac toe")
counter=0
b=0
c=0
# Create a function to handle button clicks
def button_click(b,c):
    print(f"{c}")
    print(f"{b}")

# Create a 2x7 grid of buttons
buttons = [[1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7]]
grid = [[0, 4, 4, 4, 4, 4, 4],[0, 4, 4, 4, 4, 4, 4]]
for i in range(2):
    b=0
    for j in range(7):
        if (i!=0):
            button = tk.Button(root, width=10, height=3,text=f"Blank", command=lambda b=b,c=c: button_click(b,c))
        else:
            button = tk.Button(root, width=10, height=6, text=f"Blank", command=lambda b=b, c=c: button_click(b, c))
        b=b+1
        print(f"{b}")
        button.grid(row=i, column=j)
        buttons[i][j] = button
    c = c + 1
# Start the tkinter main loop
root.mainloop()