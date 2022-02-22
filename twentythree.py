import unittest
from math import ceil, sqrt


def proper_divisors(i):
    d = [1]
    f = 2
    while f < i:
        if i % f == 0:
            d.append(f)
        f += 1
    return d


def sum_of_divisors(i):
    return sum(proper_divisors(i))


def sum_of_divisors2(i):
    if i == 1:
        return 1
    n = ceil(sqrt(i))
    total = 1
    divisor = 2
    while divisor < n:
        if i % divisor == 0:
            total += divisor
            total += i // divisor
        divisor += 1
    if n ** 2 == i:
        total += n
    return total


def is_abundant(i):
    return sum_of_divisors(i) > i


def solution(n):
    abundants = set()
    for i in range(12, n + 1):
        if is_abundant(i):
            abundants.add(i)
    abundants = list(abundants)
    abundant_sums = set()
    for j in range(len(abundants)):
        for k in range(len(abundants)):
            jk = abundants[j] + abundants[k]
            if jk < n:
                abundant_sums.add(jk)

    return int((n*(n-1)) / 2 - sum(abundant_sums))


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(12, 66)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(28123))
    unittest.main()


""" approach
generate a set of all integers less than n
generate all of the abundant numbers less than n
sum each abundant number with every other abundant number, remove this number from the set
return the set
"""

""" pseudocode
proper_divisors(i):
...

sum_of_divisors(i):
return sum(proper_divisors) - i

is_abundant(i):
return sum_of_divisors > i


solution(n):
abundants = []
nonabundants = set(range(1,n+1))
for i in range(n+1):
if is_abundant: abundants.append(i)

nonabundants.difference_update(abundants)

for j in range(len(abundants):
for k in range(j,len(abundants):
jk = abundants[j] + abundants[k]
if jk in range_n: nonabundants.remove(jk)

return sum(nonabundants)

"""
