import unittest


def sieve_of_eratosthenes(n):
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

            
primes = set(sieve_of_eratosthenes(10000))


def solution(limit):
    global primes
    max_conseq = 0
    coef_prod = 0
    for a in range(limit, -limit - 1, -1):
        for b in range(limit, -limit - 1, -1):
            n = 0
            num_conseq = 0
            res = n**2 + (a * n) + b
            while res in primes:
                num_conseq += 1
                n += 1
                res = n**2 + (a * n) + b

            if num_conseq > max_conseq:
                max_conseq = num_conseq
                coef_prod = a * b

    return coef_prod


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(41, -41)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1000))
    unittest.main()


""" approach
iterate through all values in range for coefficients, 
for each quadratic equation, evaluate number of consecutive primes generated...
"""

""" pseudocode
max_conseq = 0
coef_prod = 0
for a in range(-n,n+1):
 for b in range(-n, n+1):
   n = 0
   num_conseq = 0
   while n**2 + a*n + b in primes:
    num_conseq += 1
   if num_conseq > max_conseq:
    max_conseq = num_conseq
    coef_prod = a * b
return coef_prod

"""
