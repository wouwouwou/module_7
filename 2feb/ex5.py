# Exercise 5: Palindromes (from Project Euler 4)
# A palindromic number reads the same both ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 Ö 99.
# ! Find the largest palindrome made from the product of two 3-digit numbers.

# TODO list of all products of two 3-digit numbers, then iterate and look for palindromes, give largest one

allpalindromes=[]
highpalindrome = 90909
imax = 0
jmax = 0
i = 0
while i < 1000:
    j = 0
    while j < 1000:
        n = j * i
        n = int(n)
        if str(n) == str(n)[::-1]:
            if (n > highpalindrome):
                if (n > max(allpalindromes)):
                    imax = i
                    jmax = j
            allpalindromes.append(n)
            lastpalindrome = n
        j += 1
    i += 1

print(imax)
print(jmax)
print(max(allpalindromes))