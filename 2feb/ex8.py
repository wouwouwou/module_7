# Exercise 8: (Largest prime factors from Project Euler 3)
# The prime factors of 13195 are 5, 7, 13 and 29.

# → What is the largest prime factor of the number 600851475143?


def divisors(a):
    i = 2
    res = set()
    while i < a:
        if a % i == 0:
            res.add(i)
        i += 1
    return res


def mindivisor(a):
    i = 2
    while i < a:
        if a % i == 0:
            return i
        i += 1
    return 1


def addpf(d, a):
    if a in d.keys():
        d[a] += 1
    else:
        d[a] = 1
    return d


def upf(a):
    res = dict()

    # a number is prime if the size of the set from divisors(a) <= 2
    while mindivisor(a) != 1:
        div = int(mindivisor(a))
        res = addpf(res, div)
        a = int(a / div)
    res = addpf(res, a)
    return res


def pf(a):
    res = set()

    # a number is prime if the size of the set from divisors(a) <= 2
    while mindivisor(a) != 1:
        div = int(mindivisor(a))
        res.add(div)
        a = int(a / div)
    res.add(a)
    return res

print(divisors(6857))
print(upf(13195))
print(max(pf(600851475143)))
