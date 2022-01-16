player_1 = []
player_2 = []
Check = []
Player = [1,2,3,4,5,6,7,8,9]
win_combination = [[1,2,3], [1,4,7], [1,5,9], [2,5,8], [3,6,9], [3,5,7], [4,5,6],[7,8,9]]

def main ():
    global win_check
    win_check = 0
    while len(Check)!=9:
        get_board()
        Player_1()
        if win_check == 1:
            break
        elif win_check !=1 and len(Check)==9:
            print("This game is a draw")
            break 
        elif win_check !=1:
            get_board()
            Player_2()
            if win_check == 1:
                break
            elif win_check !=1 and len(Check)==9:
                print("This game is a draw")
                break           

def get_board():
    print (Player[0],Player[1],Player[2], sep="!")
    print ("______")
    print (Player[3],Player[4],Player[5], sep="!")
    print ("______")
    print (Player[6],Player[7],Player[8], sep="!")

def Player_1 ():
    move = int(input("Please choose the number which indicates your move: "))
    if move not in Player:
        print ("Move unavailable")
        Player_1()
    else:
        player_1.append(move)
        Player[Player.index(move)]="X"
        Check.append(move)
    Win_check (player_1, "Player 1")

def Player_2 ():
    move = int(input("Please choose the number which indicates your move: "))
    if move not in Player:
        print ("Move unavailable")
        Player_2()
    else:
        player_2.append(move)
        Player[Player.index(move)]="O"
        Check.append(move)
    Win_check (player_2, "Player 2")

def Win_check (player_turn, player_name):
    for combination in win_combination:
        Count = 0
        for i in range(3):
            for j in player_turn:
                if j == combination[i]:
                    Count+= 1
        if Count==3:
            print(f"The winner is {player_name}")
            global win_check
            win_check = 1

if __name__ == "__main__":
    main()