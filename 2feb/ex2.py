# The algorithm is as follows (in pseudo-code):
# function gcd(a, b)
# while a =/= b
# if a > b
# a := a - b;
# else
# b := b - a;
# return a;

# ! Implement the Euclidian algorithm in Python.
# To check your algorithm: the GCD of 3141 and 156 is 3.

# ! If you where to have a rectangle with size 12345678  987654321, what area would the
# largest square tile have with which you can cover the entire rectangle without leaving
# gaps?

# ! Implement a function frac which takes the arguments a and b and calculates the
# smallest form of the fraction a/b.
# Make sure b cannot be 0. Make sure your function can handle negative fractions
# properly.


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def frac(a, b):

    converta = False
    convertb = False
    inia = a
    inib = b

    if b == 0:
        return "You can not divide by 0!"

    if a == b:
        return "This is equal to one."

    if a < 0 and b < 0:
        a *= -1
        b *= -1

    if a < 0:
        converta = True
        a *= -1

    if b < 0:
        convertb = True
        b *= -1

    while gcd(a, b) != 1:
        z = gcd(a, b)
        a /= z
        b /= z

    if converta:
        a *= -1

    if convertb:
        b *= -1

    return "The smallest form of fraction " + str(inia) + "/" + str(inib) + " is " + str(int(a)) + "/" + str(int(b))

print("The gcd of 156 and 3141 is: " + str(gcd(156, 3141)))

g = gcd(12345678, 987654321)
h = 12345678 * 987654321
n = g * g
m = h / n

print("The gcd of 12345678 and 987654321 is: " + str(g))
print("Therefore the area of the square is: " + str(n))
print(frac(26, 962))
