import unittest
from math import prod

""" approach
generate a number x with 500 factors using prime decomposition 
check if x is a triangle number, by seeing if a positive integer root exists for the equation:
n^2 + n - 2x = 0
using:
n = (-1 +- sqrt(1 + 8x))/2

if no integer can be found for n ... then round?, this guarantees a triangle number...
trial division can be used to count the number of factors...

"""

""" pseudocode

"""


def number_of_factors(n):
    f = 2
    factors = {}
    while n > 1:
        if n % f == 0:
            factors[f] = factors[f] + 1 if f in factors else 2
            n //= f
        else:
            f += 1
    return prod(factors.values())


def triangle_number(m):
    return m * (m + 1) / 2


def solution(n):
    m = 1
    while number_of_factors(triangle_number(m)) < n:
        m += 1
    return triangle_number(m)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(1, 1), (6, 28)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(500))
    unittest.main()
