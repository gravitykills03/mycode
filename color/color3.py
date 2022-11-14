#!/usr/bin/env python3

import crayons

def main():

    chosencolor = input("What is your favorite color? (red, green, yellow, blue, black, magenta, cyan, white)\n>")
    chosencolor = chosencolor.lower()
    if chosencolor == "red":
        print(f"You like the color {crayons.red(chosencolor)}.")
    elif chosencolor == "green":
        print(f"You like the color {crayons.green(chosencolor)}.")
    elif chosencolor == "yellow":
        print(f"You like the color {crayons.yellow(chosencolor)}.")
    elif chosencolor == "blue":
        print(f"You like the color {crayons.blue(chosencolor)}.")
    elif chosencolor == "black":
        print(f"You like the color {crayons.black(chosencolor)}.")
    elif chosencolor == "magenta":
        print(f"You like the color {crayons.magenta(chosencolor)}.")
    elif chosencolor == "cyan":
        print(f"You like the color {crayons.cyan(chosencolor)}.")
    elif chosencolor == "white":
        print(f"You like the color {crayons.white(chosencolor)}.")
    else:
        print("Please choose a valid color next time")
main()
