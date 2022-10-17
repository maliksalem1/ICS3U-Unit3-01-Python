#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Oct 2022
# This program adds two integers


def main():
    # this function calculates area and perimeter

    # Input
    integer1 = int(input("Enter the first number to add (integer): "))
    integer2 = int(input("Enter the second number to add (integer): "))

    # Process
    total = integer1 + integer2

    # Output
    print("")
    print("{0} + {1} = {2}".format(integer1, integer2, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
