import unittest
from math import sqrt
""" approach
sieve of eratosthenes
 
"""

""" pseudocode

"""


# there's a bug in this sieve somewhere...

def solution(n):
    primes = set(range(2, n))
    for i in range(2, int(sqrt(n))):
        if i in primes:
            j = i**2
            while j < n:
                if j in primes:
                    primes.remove(j)
                j += i

    return sum(primes)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(18, 58)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(2000000))
    unittest.main()
