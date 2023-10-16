import tkinter as tk
from tkinter import *
menu = tk.Tk() #creates the menu box and sets its geometry and title
menu.geometry("400x400")
menu.title("Menu")
def start(): #starts the main method
    menu.withdraw()
    import main
    from main import root
    restart() #restarts the game buy running method
    root.mainloop() #starts the code
def restart():
    from main import restart # restarts game by running method in main called restart
    restart()
def tutorial(): #will create a tutorial image (not finished)
    import testW
#adjusts the menu by creating a text box and two buttons and places them in correct order/assigns their height
text = Label(menu, text="MANCALA GAME", fg="Red", font=("Helvetica", 18))
text.place(x=100,y=0)
start = tk.Button(menu, width=10, height=10, text=f"START",command=start)
start.place(x=150,y=50)
tutorial = tk.Button(menu, width=10, height=10, text=f"TUTORIAL",command=tutorial)
tutorial.place(x=150,y=220)
#runs a mainloop that restarts the code
menu.mainloop()


