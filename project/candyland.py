#!/usr/bin/python3
import pyfiglet
candyland = pyfiglet.figlet_format("CANDYLAND")
print(candyland)

player1 = ["Bob", "Alice", "Pedro", "Laura", "Sam"]
player2 = ["Jim", "Chuck", "Kira", "Ell", "Bre"]
begin = input("Will this be a 1 player or 2 player game?\n>")
while begin == ('1' or '2'):
    if (begin == '1'):
        enterplayer1 = input("Enter your player (Bob, Alice, Pedro, Laura, Sam):\n>")
        enterplayer1 = enterplayer1.capitalize()
        break
    elif (begin == '2'):
        enterplayer1 = input("Enter your player (Bob, Alice, Pedro, Laura, Sam):\n>")
        enterplayer2 = input("Enter your player (Jim, Chuck, Kira, Ell, Bre):\n>")
        enterplayer1 = enterplayer1.capitalize()
        enterplayer2 = enterplayer2.capitalize()
        break
    else:
        begin

spot = 0
round = 0

answer1 = " "
answer2 = " "
answer3 = " "
answer4 = " "
answer5 = " "

while round < 1 and (answer1 != ('Gumdrop' or 'Gumdrops')):
    round += 1
    print(f"Round: {round} for {enterplayer1}")
    answer1 = input('What are the squishy gelatin candies with sugar on the outside?\n>')
    answer1 = answer1.capitalize()
    if answer1 == ('Gumdrop' or 'Gumdrops'):
        spot += 6
        print("Correct! You move ahead 6 steps!")
    else :
        print("Sorry, the answer was Gumdrop. You don't get to move ahead any spaces.")
    print("Current spot: " + str(spot))

    while round < 2 and (answer2 != 'Butterfinger'):
        round += 1
        answer2 = input('Keep your hands off of my ____________! (Nestle Brand)\n>')
        answer2 = answer2.capitalize()
    if answer2 =='Butterfinger':
        spot += 12
        print("Correct! You move ahead 12 steps!")
    else :
        print("Sorry, the answer was Butterfinger. You move back 6 spaces to the beginning.")
        spot = 0
    print("Current spot: " + str(spot))

    while round < 3 and (answer3 != 'Twix'):
        round += 1
        answer3 = input("____ , Two for me, none for you!\n>")
        answer3 = answer3.capitalize()
    if answer3 == 'Twix':
        spot += 4
        print("Correct! You move ahead 4 steps!")
    elif (spot < 5):
        print("Sorry, the answer was Twix. You are lagging at the beginning of the game.")
        spot = 0
    else :
        print("Sorry, the answer was Twix. You move back 4 spaces.")
        spot -= 4
    print("Current spot: " + str(spot))

    while round < 4 and (answer4 != 'Skittles'):
        round += 1
        answer4 = input("________ , taste the rainbow!\n>")
        answer4 = answer4.capitalize()
    if answer4 == 'Skittles':
        spot += 8
        print("Correct! You move ahead 8 steps!")
    elif (spot < 9):
        print("Sorry, the answer was Skittles. You are lagging at the beginning of the game.")
        spot = 0
    else :
        print("Sorry, the answer was Skittles. You move back 8 spaces.")
        spot -= 8
    print("Current spot: " + str(spot))

    while round < 5 and (answer5 != 'York'):
        round += 1
        answer5 = input("Round pepperment pattie with dark chocolate on the outside. Shiny silver Packaging.\n>")
        answer5 = answer5.capitalize()
    if answer5 == 'York':
        spot += 4
        print("Correct! You move ahead 4 steps!")
    elif (spot < 5):
        print("Sorry, the answer was York. You are lagging at the beginning of the game.")
        spot = 0
    else :
        print("Sorry, the answer was Twix. You move back 4 spaces.")
        spot -= 4
    print("Current spot: " + str(spot))
    if (spot > 25):
        print("You have save the land of candy from all of the children who conspire to erode the contents of this magical kingdom. Congratulations!")
        print(f"Final Score: {enterplayer1} : {spot}")
    if (spot < 25):
        print("You have failed to reach the point of saving the Candy Kingdom. Better luck next time!")
        print(f"Final Score: {enterplayer1} : {spot}")
        
