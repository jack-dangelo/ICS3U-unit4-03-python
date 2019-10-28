#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: Oct 2019
# This program uses a for loop


def main():
    # this function uses a for loop
    loop_counter = 1
    # input
    positive_str = input("Enter how many times to repeat: ")
    print("")
    try:
        positive_integer = int(positive_str)
        if positive_integer < 0:
            print("That is not a valid whole integer")
            return
        # process & output
        for loop_counter in range(positive_integer + 1):
            print(" {0}² = ".format(loop_counter))
            print(" {0} ".format((loop_counter)**2))
    except Exception:
        print("That is not a valid whole integer")


if __name__ == "__main__":
    main()
