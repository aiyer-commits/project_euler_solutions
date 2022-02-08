import unittest


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


""" pseudocode
what is the largest prime factor of n
given a number... the largerst prime factor must be less than it...
takes p/2 time where p is the number of prime factors....
hmmmmm

take the sqrt of n ... 
if the sqrt is an integer... continue
else, do n mod floor(sqrt)
...

divide by a list of primes... starting with 2...
prime = [2]
stack = [n]
i = 0
if peek divisible by prime[i]: pop peek, append dividend to stack
if not, n mod prime[i], remainder...
i += 1


largest prime factor of a prime is itself... but how do you know a prime is prime...

what is a prime factorization algorithm...
find the prime factorization, then sort the list of factors

sqrt.... 
if sqrt is int, dividend is factor, append to factors
if sqrt is not int, factor is floor(sqrt) + n mod floor(sqrt)... 

every factor you find, divide remainder by all factors

"""


def solution():

    return


if __name__ == "__main__":
    unittest.main()
    print(solution())
