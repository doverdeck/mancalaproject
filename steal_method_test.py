#how to decide whose turn it is
# player one links to square ID's can only start turn with ID's whose c value coresponds with their side
# Player 1 C values = 0
# Player 2 C values = 1
# each player has their own mancala
# player 1 mancala has c-value of 0
# player 2 mancala has c-value of 1

#parameters are values updated each time the code is ran
#call the steal method within the button click
def steal_tokens( ):
        #I need the x and y cords of the button clicked, and the value
    #if the value of the last pit filled = 1 cus it was 0 before it got the last token
    #then button x,y = 0  and button x, math.abs(y-1) = 0  and mancala value adds the values of both buttons



