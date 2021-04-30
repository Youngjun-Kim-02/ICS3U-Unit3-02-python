#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: April 2021
# This program checks if guessed number is correct or wrong


def main():
    # this function checks if guessed number is correct or wrong

    # input
    print("Can you guess the number I choose from 0 to 9?")
    guessed_number = int(input("Enter the guessed number: "))
    print("")

    #process & output
    if guessed_number == 5:
        print("Correct!")
    if guessed_number != 5:
        print("Wrong!")


if __name__ == "__main__":
    main()
