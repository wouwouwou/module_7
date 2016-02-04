# TODO write function fact which gives the factorial of a number. factorial 0 = 1


def fact(n):
    if n == 0:
        return 1

    res = 1
    i = 1

    while i <= n:
        res = res * i
        i += 1

    return res


def binom(n, k):
    if n < 1 or n < k < 1:
        return "Invalid input!"

    factk = fact(k)
    factn = fact(n)
    factnmink = fact(n - k)

    return factn / (factnmink * factk)

print(fact(5))
print(binom(40, 2))
