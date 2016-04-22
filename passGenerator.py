"""Script to generate password"""

import sys
from random import *


def main():
    charUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charLower = "abcdefghijklmnopqrstuvwxyz"
    intNum = "0123456789"
    other = "!#$&*@"
    str1 = charUpper + charLower + intNum + other
    passDigit = int(raw_input("Enter no. of char/digit of your password: "))
    password = "".join(choice(str1) for i in range(passDigit))
    print "Your password is generated correctly.\n Your password is: ",password

if __name__ == '__main__':
    sys.exit(main()) 
