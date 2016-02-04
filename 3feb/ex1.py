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
    return 0


# Create a test permutation of length 20
q = testPermutation(20)
print(q)

# Define a permutation of length 10
p = [1, 2, 3, 0, 5, 4, 6, 7, 8, 9]
print(p)
printPermutation(p)
print(isTrivial(p))
print(p[0])
print(cycles(p))

# Create a trivial permutation of length 10
r = trivialPermutation(10)
print(r)
printPermutation(r)
print(r[0])
print(isTrivial(r))

# trying for cycle notation. Did understand it after using google. :D
n = [1, 2, 3, 4, 0]
printPermutation(n)

# trying to compare permutations
m = testPermutation(10)
s = trivialPermutation(10)

print(m)
print(s)
print(m == s)