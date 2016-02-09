# Implement a function composition with two arguments p and q for computing
# the composition of the two permutations p and q (represented by p  q). Test your
# implementation by typing e.g.
# 1 p = [1, 2, 3, 0, 5, 6, 4, 8, 7]
# 2 printPermutation(p)
# 3 q = composition(p, p)
# 4 printPermutation(q)
# which should yield (0,2)(1,3)(4,6,5).
# Also try it out with two dierent permutations p and q, since composition is not
# commutative: the compositions p  q and q  p are not necessarily the same!

# ! Implement a function inverse with an argument p for computing the inverse of a
# permutation p.

# ! Implement a method power with two arguments p and i, which can be used to
# compute the ith power pi of a permutation p, where i is an integer: typing power(p,
# 5) should give p5 = p  p  p  p  p.
# Ensure that the method also works for i = 0 and i < 0.

# ! Write a function period, with one argument p, that computes the smallest integer
# i  1 such that pi is the trivial permutation. Verify the correctness of the answer.

# Unless you already implemented it smartly, you may notice that your program is rather
# slow when typing e.g.:
# 1 p = testPermutation(100)
# 2 period(p)
# Improve your function period such that it yields the correct answer in a split second
# (for arbitrary permutations, including testPermutation(200)).
# (Hints: Consider cycle lengths. Study some small examples such as testPermutation(20).
# You have to use some theory that was presented earlier this week.)

from perm import *


def composition(p, q):
    return


# Create a test permutation of length 20
q = testPermutation(20)
print("\nTest permutation q of length 20: " + str(q) + "\n")

# Define a permutation of length 10
p = [1, 2, 3, 0, 5, 4, 6, 7, 8, 9]
print("Permutation p of length 10: " + str(p) + "\n")
print("Permutation p with cycle notation: ")
printPermutation(p)
print()
print("Is the permutation p trivial?")
print(isTrivial(p))
print()
print("The permutation at p[0] is: " + str(p[0]) + "\n")
print("Another cycle notation of p is: " + str(cycles(p)) + "\n")

# Create a trivial permutation of length 10
r = trivialPermutation(10)
print("The trivial permutation r is: " + str(r) + "\n")
print("Some information:")
printPermutation(r)
print(r[0])
print(str(isTrivial(r)) + "\n")

# trying for cycle notation. Did understand it after using google. :D
n = [1, 2, 3, 4, 0]
print("The permutation n is: ")
printPermutation(n)
print()

# trying to compare permutations
m = testPermutation(10)
s = trivialPermutation(10)

print("Permutation m: " + str(m))
print("Permutation s: " + str(s))
print("m equals s? ")
print(m == s)
print()

p = [1, 2, 3, 0, 5, 6, 4, 8, 7]
printPermutation(p)
# q = composition(p, p)
# printPermutation(q)