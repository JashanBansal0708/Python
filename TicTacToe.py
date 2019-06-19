board = {'top-L': " ", 'top-M': " ", 'top-R': " ",
         'mid-L': " ", 'mid-M': " ", 'mid-R': " ",
         'low-L': " ", 'low-M': " ", 'low-R': " "}

turn = "X"
winner = None

def play_game():
    global turn
    print("Game starts:")
    for i in range(9):
        display_board()
        handle_turn(turn)
        if(check_game_over()):
            display_board()
            print(turn + "'s Won")
            break
        if(turn == "X"):
            turn = "0"
        else:
            turn = "X"
    else:
        print("This is a Tie")


def display_board():
  print(board['top-L'] + "|" + board['top-M'] + "|" + board['top-R'] )
  print("-+-+-")
  print(board['mid-L'] + "|" + board['mid-M'] + "|" + board['mid-R'] )
  print("-+-+-")
  print(board['low-L'] + "|" + board['low-M'] + "|" + board['low-R'] )



def handle_turn(player):
    print(player + "'s turn.")
    position = int(input("Choose a position from 1-9: "))
    valid = False
    lookup = ["top-L", "top-M", "top-R", "mid-L", "mid-M", "mid-R", "low-L", "low-M", "low-R"]
    key = ""
    while not valid:
        while position not in [1,2,3,4,5,6,7,8,9]:
            position = int(input("Plz choose a valid position: "))
        key = lookup[position-1]
        if board[key] == " ":
            valid = True
        else:
            position = "again"
            print("This position is already filled")
    board[key] = player


def check_game_over():
    if(board["low-L"] == board["low-M"] == board["low-R"] != " "or board["mid-L"] == board["mid-M"] == board["mid-R"] != " " or board["top-L"] == board["top-M"] == board["top-R"]!= " " or board["top-L"] == board["mid-L"] == board["low-L"]!= " " or board["top-M"] == board["mid-M"] == board["low-M"]!= " " or board["top-R"] == board["mid-R"] == board["low-R"]!= " " or board["top-L"] == board["mid-M"] == board["low-R"]!= " " or board["low-L"] == board["mid-M"] == board["top-R"]!= " "):
        return True

play_game()
