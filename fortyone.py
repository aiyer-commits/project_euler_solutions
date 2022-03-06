import unittest


def sorted_digs(n):
    return sorted([int(c) for c in str(n)])


def is_pandigital(n, d):
    return sorted_digs(n) == list(range(1, d+1))


def largest_pandigital(n):
    return int(''.join([str(i) for i in range(n, 0, -1)]))


def sieve_of_eratosthenes(n):
    primes = []
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, n + 1, i))
            # the above line kills python when the number n is too large 
    return primes


def solution(n):
    lp = largest_pandigital(n)
    # print(lp)
    primes = sieve_of_eratosthenes(lp)
    # print(len(primes))
    while primes:
        p = primes.pop()
        if is_pandigital(p, n):
            return p
    return -1


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(2, -1), (3, -1), (4, 4231)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(5))
    print(solution(6))
    print(solution(7))
    print(solution(8))
    unittest.main()


""" approach
given a range of digits,
generate the largest pandigital number for that range of digits
generate all of the primes upto that number
iterate from largest prime to smallest, 
check each prime for pandigitality
return the first one that is pandigital

"""

""" pseudocode

sorted_digs(n) -> [digits]
return [int(c) for c in str(n)].sorted()


is_pandigital(n,pandigital_range)
return sorted_digs(n) == list(range(1,pandigital_range))

largest_pandigital(n):
return int(''.join([str(i) for i in range(n,0,-1)])

sieve_of_eratosthenes(n):
primes = []
multiples = set()
for i in range(2,n+1):
  if i not in primes:
   primes.append(i)
   multiples.update(range(i*i, n + 1, i))
return primes

sol(n)
lp = largest_pandigital(n)
primes = sieve_of_eratosthenes(n)
while primes:
 p = primes.pop()
 if is_pandigital(p):
  return p
return -1


"""
