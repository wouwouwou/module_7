# Exercise 3: Dierent number system
# There are a few aliens living on the Planet Mars. Humans from Earth (NASA) have set
# up communications with the aliens, using only numbers. However the communications
# are not going well: the Martians use another number system. You must help NASA
# communicating with the aliens.

# ! Write a function encode that converts a number between 0 and 35 to a number or
# (capital) letter.
# For example, input 0 must return 0, input 8 must return 8 and input 35 must return
# Z.

# ! Write a function toK that takes a positive number n (in the decimal system) and an
# integer 2  k  35 and converts it to a string in a k-digit number system.
# For example: the input n = 100; k = 10 must return 100 and the input n = 4321; k =
# 16 must return 10E1.

# ! Write a function decode that converts a string containing one number (0-9) or letter
# (A-Z) to a number between 0 and 35. The function must be the inverse of encode.

# ! Write a function fromK with two arguments s and k that converts a string of letters
# and numbers s from a k-digit number system to the decimal number system. The
# function must be the inverse of toK.

# Use the functions toK and fromK to create a function convert with arguments,
# k, m and s, which converts the string s from a k-digit decimal system to an m-digit
# decimal system.
# For example: the input k = 2;m = 4 and s = 10011010 outputs 2122, and the
# input k = 16;m = 7 and s = B48C03 is 202400366.

import math

def encode(a):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if a < 0:
        return "Give a number which is at least 0!"
    if a > 35:
        return "Give a number which is less than 35!"
    if a < 10:
        return str(a)
    return str(alphabet[(a-10)])


def decode(b):
    alphdict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19,
                "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
                "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}

    if type(b) == str:
        for key in alphdict:
            if b == key:
                return alphdict[key]
        return "De input is niet geldig!"


def toK(n, k):

    res = ""

    while n >= k:
        res = str(encode(n % k)) + res
        n -= n % k
        n /= k
        n = int(n)

    if n > 0:
        res = str(encode(n)) + res

    return res


def fromK(s, k):

    res = 0
    i = 0

    for a in reversed(s):
        res += (int(decode(a)) * int(math.pow(k, i)))
        i += 1
    return res


def convert(k, m, s):
    return toK(fromK(s, k), m);


print(encode(35))
print(decode("T"))
print(toK(4321, 16))
print(fromK("10E1", 16))
print(convert(16, 7, "B48C03"))

