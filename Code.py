#------- Gobal Variable --------


# GameBoard
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if fame is still going
game_is_still_going = True

# Whose turn 
current_player = "X"  

# Winner and tie
winner = None

# displayBoard

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])



# flip player

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  else :
    current_player = "X"
    return 
# check win
    
def check_if_win():
    
    global winner
    
    # check rows
    winner_row = check_rows()
    # check columns
    winner_column = check_columns()
    # chectak diagonals
    winner_diagonal = check_diagonals()
    if winner_row:
        winner = winner_row
    elif winner_column:
        winner = winner_column
    elif winner_diagonal:
        winner = winner_diagonal
    else:
        winner = None
    return winner
    
def check_rows():
    
    global game_is_still_going
    
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_is_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return None

def check_columns():
    global game_is_still_going
    
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_is_still_going = False
    if column_1 :
        return board[0]
    if column_2 :
        return board[1]
    if column_3 :
        return board[2]
    return None

def check_diagonals():
    
    global game_is_still_going
    
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2 :
        game_is_still_going = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return None

# check tie

def check_if_tie():
  global game_is_still_going
  if "-" not in board :
    game_is_still_going = False
  return
    
def check_if_game_over():
    check_if_win()
    check_if_tie()
    
# handle turn
def handle_turn(player):
    print("Player "+player+"'s turn")
    position = input("Choose from 1-9: ")
    valid =  False
    while not valid:  
      while position not in ["1","2","3","4","5","6","7","8","9"] :
        position = input("Choose from 1-9: ")
      position = int(position)-1
      if board[position] == "-":
        valid = True
      else:
        print("The position is occupied try again!")
    # print(position)
    board[position] = player
    display_board()

    
# Play a game of TicTacToe
def play_game():
    
    #Display initial board
    display_board()
    
    while game_is_still_going:
        
        handle_turn(current_player)
        
        check_if_game_over()
        
        flip_player()
        
    # The game has ended
    if winner == "X" or winner == "O":
        print("The winner is : "+winner)
    elif winner == None:
        print("Tie.")


play_game()

