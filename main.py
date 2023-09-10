#To check which player is playing.
def player_call(player):
    if player=="A":
        print("A is playing.") 
    if player=="B":
        print("B is playing.")

# To edit the list with X and 0 
def player_play(game_list,sym):
    
    ask_row=int(input("Enter the position[row]: "))
    ask_col=int(input("Enter the position[column]: "))
    if game_list[ask_row][ask_col]=="":
        game_list[ask_row][ask_col]=sym
    else:
        print("Invalid move!")
        # The `exit(1)` statement is used to exit the program with a status code of 1(generally used to depict error). In this case,
        # it is used to terminate the program if an invalid move is made.
        exit(1)
   
# To check if either is winning.
def game_win(game_list,sym):
    for row in game_list:#row wise
        #The all() function returns True if all items in an iterable are true, otherwise it returns False.
        #If the iterable object is empty, the all() function also returns True.
        if all(cell == sym for cell in row):
            return True

    for col in range(3):#column wise
        if all(game_list[row][col] == sym for row in range(3)):
            return True

    if all(game_list[i][i] == sym for i in range(3)) or all(game_list[i][2 - i] == player for i in range(3)):#First there is left-diagonal and Second there is right diagonal
        return True

    return False
    
#To check if game is a draw.
def game_draw(li):
    return  all(li[i][j] != "" for i in range(3) for j in range(3))
    # The expression `all(li[i][j] != "" for i in range(3) for j in range(3))` is checking if
    # all the cells in the game board are filled with a symbol (either "X" or "O").
    
#To display the changes made after every move.
def display(li):
    for i in li:
        for j in i:
            print("\t",j,"\t||",end="")
        print("\n")

#main
play=True
while play:
    inp1=input("""Do you want to play Tic-Tac-Toe? 
           Type y for yes and n for no. """)
    if inp1=="y":
        print(""" 

                          ||            ||
                   0,0    ||    0,1     ||   0,2
                          ||            ||
                          ||            ||
              =====================================
                          ||            ||              Let's start the game 
                   1,0    ||     1,1    ||   1,2        Player A : X
                          ||            ||              Player B : O
                          ||            ||              
              =====================================
                          ||            ||
                   2,0    ||    2,1     ||   2,2
                          ||            ||
                          ||            || """)
        game_ini=[["","",""],["","",""],["","",""]]
        player="A"
        sym="X"
        while True:
            player_call(player)
            player_play(game_ini,sym)
            display(game_ini)
            if game_win(game_ini,sym):
                    display(game_ini)
                    print("Player ",player, "won the game!")
                    break
            if game_draw(game_ini):
                    display(game_ini)
                    print("It's a draw!.")
                    break
            if player=="A" and sym=="X":
                player="B" 
                sym="O"
            else:
                player="A"
                sym="X"
    elif inp1 == "n":
        print("Done")
        play=False
    else:
        print("Wrong input")
