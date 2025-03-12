# Tic-Tac-Tac game
def TicTacToe():
    def TTT():
        def sum(x , y , z):    # A Function To Add More Than Two Values
            return x + y + z
            
        # Lists to Set X and O
        Xsheet = [0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0]      
        Osheet = [0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0]
        turn = 1

        def playing_board():
            # Positions on the board
            zero = "X" if Xsheet[0] else "O" if Osheet[0] else 0
            one = "X" if Xsheet[1] else "O" if Osheet[1] else 1
            two = "X" if Xsheet[2] else "O" if Osheet[2] else 2
            three = "X" if Xsheet[3] else "O" if Osheet[3] else 3
            four = "X" if Xsheet[4] else "O" if Osheet[4] else 4
            five = "X" if Xsheet[5] else "O" if Osheet[5] else 5
            six = "X" if Xsheet[6] else "O" if Osheet[6] else 6
            seven = "X" if Xsheet[7] else "O" if Osheet[7] else 7
            eight = "X" if Xsheet[8] else "O" if Osheet[8] else 8
            
            '''
              1  |  2  | 3
            -----|-----|-----
              4  |  5  |  6
            -----|-----|-----
              7  |  8  |  9
            '''
            # Prints The Board
            print(f'''                                      
              {zero}  |  {one}  |  {two}
            -----|-----|-----
              {three}  |  {four}  |  {five}
            -----|-----|-----
              {six}  |  {seven}  |  {eight}
            ''')

        # Checks The Result Of the Game
        def checkResult():
            playing_board()
            Wins = [[0 ,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
            
            for win in Wins:
                if sum(Xsheet[win[0]] , Xsheet[win[1]] , Xsheet[win[2]]) == 3:
                    print(f"X wins!")
                    return 1
                elif sum(Osheet[win[0]] , Osheet[win[1]] , Osheet[win[2]]) == 3:
                    print(f"O wins!")
                    return 0
            IfDraw = [o + x for o, x in zip(Osheet, Xsheet)]
            if IfDraw == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
                print("Match is a Draw")
                return 2
            return -1
                
        # Game Starts
        while True:
            # Shows The Game Board
            playing_board()
            # X has First Turn
            if turn == 1:
                print("X's turn")
                try:
                    choice = int(input("Enter the position: ")) # Takes The Position
                    if choice < 0 or choice > 8:            # Checks If The Position Is Valid
                        print("Please Enter The Correct Position")
                    else:
                        if Xsheet[choice] == 1 or Osheet[choice] == 1:  # Check If The Position Is Already Taken
                            print("Position already taken")
                            turn = 0
                        else:
                            Xsheet[choice] = 1                           # Insert X In The Position
                except:
                    print("Invalid input")
            else:
                print("O's turn")
                try:
                    choice = int(input("Enter the position: "))     # Takes The Position
                    if choice < 0 or choice > 8:                    # Checks If The Position Is Valid
                        print("Please Enter The Correct Position")
                    else:
                        if Xsheet[choice] == 1 or Osheet[choice] == 1:      # Check If The Position Is Already Taken
                            print("Position already taken")
                            turn = 1
                        else:
                            Osheet[choice] = 1                          # Insert O In The Position
                except:
                    print("Invalid input")
                
            try:
                winner = checkResult()
                if winner != -1:        # Breaks If The Result Is Decided
                    break
            except Exception as e:
                print(e)
            
            turn = 1 if turn == 0 else 0        # Switches The Turn
    while True:
        TTT()       # Calls The Game Function
        replay = input("Do you want to play again? (yes/no): ").strip().lower()     # Asks If The Player Wants To Play Again
        play_again = ["yes", "y" , "yeah", "yup", "sure", "ok", "okay","yea", "ya", "yep"]
        if replay not in play_again:            # Breaks If The Player Does Not Want To Play Again
            print("Thanks for playing! Goodbye!")
            break
        
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe game!")       # Welcome Message
    TicTacToe()                                 # The Game Begins