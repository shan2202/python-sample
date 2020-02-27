
def display_board(board):
    print("-\t-\t-")
    print(board[1]+"\t" + board[2] +"\t" + board[3])
    print("-\t-\t-")
    print(board[4]+"\t" + board[5] +"\t" + board[6])
    print("-\t-\t-")
    print(board[7]+"\t" + board[8] +"\t" + board[9])

def player_input(board):
    pos = int(input("Enter the position : "))
    val = input("Enter X or O : ")
    board[pos] = val
    return board
def check_win(board):
    pass

#test_board = ['#','X','O','X','O','X','O','X','O','X']
test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)
player_board = player_input(test_board)
display_board(player_board)


