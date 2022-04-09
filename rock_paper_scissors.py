import random
import re
p_wins = 0
c_wins = 0


def check_result(player, computer, pl_wins, co_wins):
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
        pl_wins += 1
    elif win == 2:
        winner = "Computer wins!"
        co_wins += 1
    else:
        winner = "It's a tie!"

    return winner, pl_wins, co_wins


while 1 < 2:
    print("\n----------------------")
    print("Rock, Paper, Scissors - Go!")
    user_opt = input("Select: [R]ock, [P]aper, [S]cissors: ")

    if re.match("[RrPpSs]", user_opt):
        print("Your selection: %s " % user_opt.upper())
        choices = ["R", "P", "S"]
        computer_opt = random.choice(choices)
        print("Computer chose: %s " % computer_opt)
        result = check_result(user_opt, computer_opt, p_wins, c_wins)
        print(result[0])
        p_wins = result[1]
        print("Player wins: %s" % p_wins)
        c_wins = result[2]
        print("Computer wins: %s" % c_wins)
        if p_wins == 2 or c_wins == 2:
            break
    else:
        print("Error, select one letter")
