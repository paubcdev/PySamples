import random
import re
game_count = 0


def check_result(player, computer):
    win = 0
    if(player.upper() == "R" and computer == "R") or (player.upper() == "P" and computer == "P") or\
            (player.upper() == "S" and computer == "S"):
        win = 3
    elif(player.upper() == "R" and computer == "S") or (player.upper() == "S" and computer == "P") or\
            (player.upper() == "P" and computer == "R"):
        win = 1
    elif(player.upper() == "R" and computer == "P") or (player.upper() == "S" and computer == "R") or \
            (player.upper() == "P" and computer == "S"):
        win = 2

    if win == 1:
        winner = "Player wins!"
    elif win == 2:
        winner = "Computer wins!"
    else:
        winner = "It's a tie!"

    return winner


while game_count < 3:

    print("Rock, Paper, Scissors - Go!")
    user_opt = input("Select: [R]ock, [P]aper, [S]cissors: ")

    if re.match("[RrPpSs]", user_opt):
        print("Your selection: %s " % user_opt.upper())
        computer_opt = ["R", "P", "S"]
        ch = random.choice(computer_opt)
        print("Computer chose: %s " % ch)
        result = check_result(user_opt, ch)
        print(result)
        game_count += 1
    else:
        print("Error, select one letter")
