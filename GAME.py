import mysql.connector as mys
import random
mycon=mys.connect(host='localhost',user='root',passwd='2130',database='Handgame')
#if mycon.is_connected():
    #print("Succesfully connected")
mycursor=mycon.cursor()
#mycursor.execute("Create table RPS(NAME varchar(30),YOUR_SCORE int(10),COMPUTERS_SCORE int(10),RESULT VARCHAR(10))")
#mycursor.execute("Create table HC(NAME varchar(30),YOUR_SCORE int(10),COMPUTERS_SCORE int(10),RESULT VARCHAR(10))")

def rps():
    player_points = 0
    computer_points = 0
    print("!"*30,"WELCOME TO ROCK-PAPER-SCISSORS","!"*30)
    a=input("ARE YOU READY TO PLAY????(Y/N): ")
    if a.upper()=="Y":
        print("!"*25," LET'S START THE GAME","!"*25)
        print('''Rock, Paper, Scissors Game Rules:
->Players enter 'R' for Rock, 'P' for Paper, or 'S' for Scissors.
->The game runs until one player reaches 5 points.
->Each round, choices are compared: ties result in a draw, and different choices determine the winner. 
->The first to 5 points wins the game.''')
        print("PLEASE ENTER YOUR NAME: ")
        nm=input()
        print("_"*75)

        while (player_points < 5 and computer_points < 5):
            print("Rock, Paper, Scissors - Enter your choice (R/P/S): ")
            player_choice = input().upper()

            if player_choice not in ['R', 'P', 'S']:
                print("Invalid choice. Please enter R for Rock, P for Paper, or S for Scissors.")
                continue

            computer_choice_number = random.randint(0, 2)  # 0 for Rock, 1 for Paper, 2 for Scissors
            computer_choice = 'R' if computer_choice_number == 0 else ('P' if computer_choice_number == 1 else 'S')
            print("Computer chose:", computer_choice)

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (
                (player_choice == 'R' and computer_choice == 'S') or
                (player_choice == 'P' and computer_choice == 'R') or
                (player_choice == 'S' and computer_choice == 'P')):
                print("You win this round!")
                player_points += 1
            else:
                print("Computer wins this round!")
                computer_points += 1

            print("Player:", player_points, "| Computer:", computer_points)
            print()
        if player_points >= 5:
            r="WON"
            print("You win the game!")
        else:
            r="LOSS"
            print("Computer wins the game!")
        print("*"*30,"THANKS FOR PLAYING","*"*30)
        qry="insert into RPS values(%s,%s,%s,%s)"
        l=[nm,player_points,computer_points,r]
        mycursor.execute(qry,l)
        mycon.commit()
        print("RECORD ADDED")


def play_hand_cricket():
    user_score = 0
    computer_score = 0
    max_turns = 6

    print("!"*30, "WELCOME TO HAND CRICKET GAME", "!"*30)
    a = input("ARE YOU READY TO PLAY????(Y/N): ")

    if a.upper() == "Y":
        print("!"*25, " LET'S START THE GAME", "!"*25)
        print('''Hand Cricket Game Rules:
->Score runs by choosing numbers (1-6) during batting; avoid getting out by guessing computer's number during bowling.
->The game has two phases for the player and computer.
->The player with the highest total score after six turns wins.
->The computer wins if it surpasses the player's score during the player's bowling phase.''')
        print("PLEASE ENTER YOUR NAME: ")
        nm = input()
        print("_"*75)

        # Toss
        toss_result = random.choice(["Heads", "Tails"])
        print("Let's toss to decide who bats first.")
        user_call = input("Heads or Tails? ").capitalize()

        if user_call == toss_result:
            print(f"{nm} won the toss!")
            batting_first = True
        else:
            print("Computer won the toss.")
            batting_first = False

        print("_"*75)

        # Batting and Bowling based on the toss result
        if batting_first:
            user_score = user_batting(computer_score, max_turns, nm)
            computer_score = computer_batting(user_score, max_turns, nm)
        else:
            computer_score = computer_batting(user_score, max_turns, nm)
            user_score = user_batting(computer_score, max_turns, nm)

        check_winner(user_score, computer_score, nm)

def user_batting(computer_score, max_turns, nm):
    user_score = 0

    print("\nYour batting:")
    for turn in range(1, max_turns + 1):
        print(f"Turn {turn}: Enter a number between 1 and 6:")
        user_choice = get_valid_input()

        computer_choice = random.randint(1, 6)
        print(f"Computer's bowling: {computer_choice}")

        if user_choice != computer_choice:
            user_score += user_choice
            print(f"Your score: {user_score}")
            if computer_score!= 0 :
                if user_score> computer_score:
                    print("u win")
                    break

        else:
            print("Out! Your batting ends.")
            break

    print("\nYour final score:",user_score)
    return user_score

def computer_batting(user_score, max_turns, nm):
    computer_score = 0

    print("\nComputer's batting:")
    for turn in range(1, max_turns + 1):
        computer_choice = random.randint(1, 6)
        
        print(f"Turn {turn}: Enter a number between 1 and 6:")
        user_choice = get_valid_input()

        print(f"Computer's batting: {computer_choice}")

        if user_choice != computer_choice:
            computer_score += computer_choice
            print(f"Computer's score: {computer_score}")
            if user_score!=0:
                if computer_score > user_score:
                    print("Computer wins. Better luck next time!")
                    break
        else:
            print("Out! Computer's batting ends.")
            break

    print("\nComputer's final score: ",computer_score)
    return computer_score

def get_valid_input():
    while True:
        try:
            user_choice = int(input())
            if 1 <= user_choice <= 6:
                return user_choice
            else:
                print("Invalid input. Enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 6.")

def check_winner(user_score, computer_score, nm):
    if user_score > computer_score:
        r="WoN"
        print(f"Congratulations {nm}! You win!")
    elif user_score < computer_score:
        r="LOSS"
        print("Computer wins. Better luck next time!")
    else:
        r="TIE"
        print("It's a tie!")
    print("*"*30, "THANKS FOR PLAYING", "*"*30)
    qry="insert into HC values(%s,%s,%s,%s)"
    l=[nm,user_score,computer_score,r]
    mycursor.execute(qry,l)
    mycon.commit()
    print("RECORD ADDED")
print()

import turtle
import time
def exit():
# Create a new turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor("black")

# Create a new turtle object
    t = turtle.Turtle()
    t.color("white")

# Function to draw a rectangle with rounded corners
    def rounded_rect(t, width, height, corner_radius):
        t.pendown()
        for _ in range(2):
            t.forward(width - 2 * corner_radius)
            t.circle(corner_radius, 90)
            t.forward(height - 2 * corner_radius)
            t.circle(corner_radius, 90)
        t.penup()
    time.sleep(5)
    # Draw the sign
    t.penup()
    t.goto(-200, -100)  # this will center the rectangle
    rounded_rect(t, 440, 220, 30)

    def bold_text(t, text, font, x, y):
        t.penup()
        for i in range(-2, 3):
            for j in range(-2, 3):
                t.goto(x + i, y + j)
                t.write(text, font=font)
        t.penup()

    # Write GAME OVER
    bold_text(t, "GAME OVER", ("Arial", 48, "normal"), -210, 0)

# Draw a line
    t.goto(-205, -5)
    t.pendown()
    t.forward(400)
    t.penup()

    t.goto(-200, -60)
    t.write("Thanks for playing", font=("Arial", 32, "normal"))

# Hide the turtle and keep the window open
    t.hideturtle()
    turtle.done()

print("!"*30," WELCOME TO HANDGAMES  ","!"*30)
while True:
    opt=int(input('''WHAT WOULD YOU LIKE TO DO:-
1. PLAY ROCK-PAPER-SCISSORS
2. PLAY HAND CRICKET
3. EXIT 
PLEASE ENTER YOUR CHOICE: '''))
    if opt==1:
        rps()
        print("_"*70)
    elif opt==2:
        play_hand_cricket()
        print("_"*70)
    elif opt==3:
        exit()
        print("*"*30,"THANKS FOR PLAYING","*"*30)
        break

    else:
        print("PLEASE ENTER ANY VALID OPTION")
    

