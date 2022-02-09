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


def all_factors(i):
    s = []
    f = 2
    while f < i:
        if i % f == 0:
            s.append(f)
        f += 1
    return s


def solution(nu):
    n0, n1 = nu
    prodd = 1
    factors = set(1)
    for i in range(n0,n1):
        if i in factors:
            continue
        else:
            prodd *= i
            
    return


if __name__ == "__main__":
    # unittest.main()
    print(solution([1, 11]))
