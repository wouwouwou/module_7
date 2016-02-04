# → Write a function that gets as input an integer a and computes as output the set of all
# integer divisors of a.

# → Write a function that gets as input an integer a and computes as output the unique
# prime factorization of a. (One possibility is to store the output in a dictionary, with
# as key the prime factor and as value its multiplicity.)


def divisors(a):
    i = 2
    res = set()
    while i < a:
        if a % i == 0:
            res.add(i)
        i += 1
    return res


def addpf(d, a):
    if a in d.keys():
        d[a] += 1
    else:
        d[a] = 1
    return d


def upf(a):
    res = dict()

    # a number is prime if the size of the set from divisors(a) <= 2
    while divisors(a).__len__() != 0:
        div = int(min(divisors(a)))
        res = addpf(res, div)
        a = int(a / div)
    res = addpf(res, a)
    return res

print(divisors(12))
print(upf(12))

