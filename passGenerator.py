"""Script to generate password"""

import sys
import random


def main():
    charUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charLower = "abcdefghijklmnopqrstuvwxyz"
    intNum = "0123456789"
    other = "!#$&*@"
    str1 = charUpper + charLower + intNum + other
    passDigit = int(input("Enter no. of char/digit of your password: "))
    password = "".join(random.choice(str1) for i in range(passDigit))
    print("Your password is generated correctly.\nYour password is: ",password)

if __name__ == '__main__':
    sys.exit(main())
