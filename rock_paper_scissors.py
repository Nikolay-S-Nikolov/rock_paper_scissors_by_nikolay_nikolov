import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_choose = "yes"
draw_counter = 0
win_counter = 0
loose_counter = 0

while player_choose == "yes":
    computer_move = ""
    player_move = input("Choose [r] for rock, [p] for paper"
                        " or [c] for scissors and press [enter]:")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "c":
        player_move = scissors
    else:
        print("Invali input.Try again...")
    computer_random_number = random.randint(1, 3)
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(f"The computer chose {computer_move}.")
    if computer_move == player_move:
        print("Draw")
        draw_counter +=1

    elif (computer_move == scissors and player_move == rock) or \
            (computer_move == paper and player_move == scissors) or \
            (computer_move == rock and player_move == paper):
        print("You win!")
        win_counter+=1
    else:
        print("You loose!")
        loose_counter+=1
    print(f"You win {win_counter} times, "
          f"loose {loose_counter} times and"
          f" the game was draw {draw_counter} times")

    player_choose = input("Type [yes] to play again or [no] to quit:")
