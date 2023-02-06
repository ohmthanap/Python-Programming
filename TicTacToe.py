# Created by: Thanapoom Phatthanaphan
# This program is the Tic-Tac-Toe game, it shows the instruction,
# displays the game screen, and also judge the result of the game

from turtle import Turtle


def instructions():
    # this function prints the instructions
    print("""
        Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
        This will be a showdown between your human brain and my silicon processor.

        You will make your move known by entering a number, 0 - 8. The number
        will correspond to the board position as illustrated:

        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8

        Prepare yourself, human. The ultimate battle is about to begin. \n
        """)


def draw_board():
    # this function draws Tic-Tac-Toe board
    t.width(2)
    for i in range(4):
        t.forward(300)
        t.left(90)
    t.setheading(0)
    t.up()
    t.goto(100, 0)
    t.left(90)
    t.down()
    t.forward(300)
    t.up()
    t.goto(200, 0)
    t.down()
    t.forward(300)
    t.up()
    t.right(90)
    t.goto(0, 100)
    t.down()
    t.forward(300)
    t.up()
    t.goto(0, 200)
    t.down()
    t.forward(300)
    t.up()
    t.setheading(0)


def draw_o(x, y):
    # this function draws a circle symbol when player select a position
    t.pencolor('green')
    t.goto(x, y - 40)
    t.down()
    t.circle(40)
    t.up()


def draw_x(x, y):
    # this function draws an 'X' symbol when player select a position
    t.pencolor('red')
    t.goto(x - 35, y + 35)
    t.down()
    t.goto(x + 35, y - 35)
    t.up()
    t.goto(x + 35, y + 35)
    t.down()
    t.goto(x - 35, y - 35)
    t.up()


def play_game():
    # this function runs the Tic Tac Toe Game and judge the result of the game
    while True:
        player1 = int(input("Select symbol for Player 1 (Press 1 for X, Press 2 for O): "))
        if player1 == 1:
            player1 = 'X'
            player2 = 'O'
            break
        elif player1 == 2:
            player1 = 'O'
            player2 = 'X'
            break
        else:
            print("You selected a wrong symbol")
    print("Player 1 is " + player1 + " and Player 2 is " + player2)

    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    count = 0
    while True:
        while count < 9:
            num_selected = int(input("Player 1 enters number 0-8: "))
            if num_selected in number_list:
                checkBoard[num_selected] = player1
                number_list.remove(num_selected)
                if player1 == 'X':
                    draw_x(xAxis_inBoard[num_selected], yAxis_inBoard[num_selected])
                else:
                    draw_o(xAxis_inBoard[num_selected], yAxis_inBoard[num_selected])
                count += 1
                break
            else:
                print("Player 1 entered a wrong number")

        if ((checkBoard[0] == checkBoard[1] == checkBoard[2] == player1) or
                (checkBoard[3] == checkBoard[4] == checkBoard[5] == player1) or
                (checkBoard[6] == checkBoard[7] == checkBoard[8] == player1) or
                (checkBoard[0] == checkBoard[3] == checkBoard[6] == player1) or
                (checkBoard[1] == checkBoard[4] == checkBoard[7] == player1) or
                (checkBoard[2] == checkBoard[5] == checkBoard[8] == player1) or
                (checkBoard[0] == checkBoard[4] == checkBoard[8] == player1) or
                (checkBoard[2] == checkBoard[4] == checkBoard[6] == player1)):
            print("Player 1 is the winner!")
            break

        while count < 9:
            num_selected = int(input("Player 2 enters number 0-8: "))
            if num_selected in number_list:
                checkBoard[num_selected] = player2
                number_list.remove(num_selected)
                if player2 == 'X':
                    draw_x(xAxis_inBoard[num_selected], yAxis_inBoard[num_selected])
                else:
                    draw_o(xAxis_inBoard[num_selected], yAxis_inBoard[num_selected])
                count += 1
                break
            else:
                print("Player 2 entered a wrong number")

        if ((checkBoard[0] == checkBoard[1] == checkBoard[2] == player2) or
                (checkBoard[3] == checkBoard[4] == checkBoard[5] == player2) or
                (checkBoard[6] == checkBoard[7] == checkBoard[8] == player2) or
                (checkBoard[0] == checkBoard[3] == checkBoard[6] == player2) or
                (checkBoard[1] == checkBoard[4] == checkBoard[7] == player2) or
                (checkBoard[2] == checkBoard[5] == checkBoard[8] == player2) or
                (checkBoard[0] == checkBoard[4] == checkBoard[8] == player2) or
                (checkBoard[2] == checkBoard[4] == checkBoard[6] == player2)):
            print("Player 2 is the winner!")
            break
        elif count == 9:
            print("It's a tie!")
            break
        else:
            continue


print("Here are the instructions to the Tic-Tac-Toe game:")
instructions()
print("Here are the instructions a second time:")
instructions()
print("You probably understand the game by now.")
input("Press 'enter' to continue... ")
t = Turtle()
t.hideturtle()
t.speed(300)
checkBoard = [' ', ' ', ' ',
              ' ', ' ', ' ',
              ' ', ' ', ' ']
xAxis_inBoard = (50, 150, 250, 50, 150, 250, 50, 150, 250)
yAxis_inBoard = (250, 250, 250, 150, 150, 150, 50, 50, 50)
draw_board()
play_game()
input("Press any button to close the program... ")
