import unittest

""" approach
generate the primes less than n, and sum them
p = [2,3,5,7,11,13]
is_prime(m)
for prime in p:
if n mod p == 0:
return False

return True

get_primes_lt(n):
for i in range(n)
if is_prime(i)
p.append(i)
else
continue

solution(n)
get_primes(n)
return sum(p)

"""

""" pseudocode

"""


def is_prime(m):
    for p in primes:
        if m % p == 0:
            return False
    return True


def primes_lt(n):
    for i in range(14, n):
        if is_prime(i):
            primes.append(i)


primes = [2, 3, 5, 7, 11, 13]


def solution(n):
    assert(n > 13)
    primes_lt(n)
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
