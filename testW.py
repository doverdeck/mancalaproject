#how to decide whose turn it is
# player one links to square ID's can only start turn with ID's whose c value coresponds with their side
# Player 1 C values = 0
# Player 2 C values = 1
# each player has their own mancala
# player 1 mancala has c-value of 0
# player 2 mancala has c-value of 1

import tkinter as tk
import random


def change_button_color():
    # Generate a random color (you can set your own color logic here)
    random_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Configure the button's background color
    red_button.config(bg=random_color)


# Create a tkinter window
window = tk.Tk()
window.title("Change Button Color Example")

# Create an initial red-colored button
red_button = tk.Button(window, text="Change Color", bg="red", fg="red", command=change_button_color)
red_button.pack()

# Start the Tkinter main loop
window.mainloop()
