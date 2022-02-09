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
get the product of all of the semiprimes
remove their primes from their set
multiply remaining primes by the product


disjoint(sett)

"""


def factors(i):
    s = [1]
    f = 2
    while i > 1:
        if i % f == 0:
            s.append(f)
            i //= f
        else:
            f += 1
    return s


def solution(nu):
    n0, n1 = nu
    p, s = set(), {}
    
    for i in range(n0, n1):
        f = factors(i)
        if len(f) > 2:
            s[i] = f
        else:
            p.add(i)

    for pr in p:
        for (se, v) in s:
            if pr in v:
                p.remove(pr)
                break
    
        

        
    return prod(prod(s.keys()), p)


if __name__ == "__main__":
    unittest.main()
    print(solution())
