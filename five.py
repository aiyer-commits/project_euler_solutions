import unittest
from math import prod


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [([1, 11], 2520)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


""" pseudocode
what is the smallest multiple of the numbers 1-20

given a set of primes and their semiprimes n0 <= i <= n1
disjoint the set into a set of primes and semiprimes
get all semiprimes
remove all semiprimes that are factors of other semiprimes
remove prime factors of 'multiple semiprimes'
multiply remaining primes by the product


disjoint(sett)

"""


def prime_factors(i):
    hm = {}
    f = 2
    while i > 1:
        if i % f == 0:
            if f in hm:
                hm[f] += 1
            else:
                hm[f] = 1
            i //= f
        else:
            f += 1
    return hm


def solution(nu):
    n0, n1 = nu
    factors = {}
    for i in range(n0, n1):
        hm = prime_factors(i)
        for f in hm.keys():
            if f in factors.keys():
                if hm[f] > factors[f]:
                    factors[f] = hm[f]
            else:
                factors[f] = hm[f]
    prodd = 1
    for f in factors.keys():
        prodd *= f**factors[f]
    print(factors)
    return prodd 


if __name__ == "__main__":
    # unittest.main()
    print(solution([1, 21]))
