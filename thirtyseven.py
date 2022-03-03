import unittest


primes = set()


def sieve(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            primes.add(i)
            multiples.update(range(i*i, n+1, i))
    return


def is_prime(n):
    global primes
    if n in primes:
        return True
    return False


def is_truncatable(p):
    div = 10
    while div < p:
        if not is_prime(p % div) or not is_prime(p // div):
            return False
        div *= 10
    return True


def solution():
    truncatable_primes = set()
    i = 23
    while len(truncatable_primes) < 11:
        if is_prime(i) and is_truncatable(i):
            truncatable_primes.add(i)
            print(truncatable_primes)
        i += 2
    return sum(list(truncatable_primes))


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    sieve(1000000)
    print(solution())
    # unittest.main()


""" approach
starting at 3, append one of (1,3,5,7,9), check if the result is prime
if it is, add it to the list of truncatable primes
go through this list and repeat the process, until all of the numbers are exhausted
should be 11 total truncatable primes...
"""

""" pseudocode
is_prime(n):
 f = 2
 while f < n:
  if n % f:
   return False
  f += 1
 return True

append_digit(d, n):
return int(''.join([c for c in str(n)])+str(d))

append_left_digit(d, n):
return int(str(d) + ''.join([c for c in str(n)]))

sol(n):
 prime_digs = [3, 7, 9]
 truncatable_primes = set([37,79])
 queue = deque(list(truncatable_primes))
 while queue:
  value = queue.popleft()
  if isPrime(value):
   queue.extend([append_left_digit(d, value) for d in prime_digs])
   queue.extend([append_digit(d, value) for d in prime_digs])
   truncatable_primes.append(value)
 assert(len(truncatable_primes) == 11)
 return sum(truncatable_primes)
  
"""
