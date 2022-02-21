import unittest
from math import sqrt

""" approach
n < 10000


'one' and the primes are amicable numbers...
get all primes using sieve of eratosthenes

then factorize each remaining number using trial division
but, generate a list of proper divisors in the process
sum that list of proper divisors... 
if this number is in the remaining numbers...
factorize, sum proper divisors, and test equivalence.. is_amicable
if not is_amicable.... remove the first number, test the resultant number...


"""

""" pseudocode

proper_divisors(m):
divisors = {1:1}
d = 1
proper = []
while m > 1:

if m % d == 0:
divisors[d] = 1 if d not in divisors else divisors[d] + 1
d /= f
else:
d += 1

for k in divisors:
n = divisors[k]
while n > 0:
proper.append(k*n)
n -= 1

return proper

d(n):
return sum(proper_divisors(n))

is_amicable(m,n):
if d(m) == n:
return True
else return False

solution(i)
amicables = set([1])
amicables.update(sieve_of_eratosthenes(n))
sett = set(range(2,n+1))
sett.difference_update(amicables)
for n in sett:
m = d(n)
if is_amicable(m,n): amicables.add(m)

return sum(amicables)

sieve_of_eratosthenes(n):
primes = set(range(2,n))
for i in range(2, int(sqrt(n))):
if i in primes:
j = i**2
while j < n:
if j in primes:
primes.remove(j)
j+=i
return primes

"""


def proper_divisors(i):
    f = 2
    divisors = [1]
    while f < i:
        if i % of == 0:
            divisors.append(f)
        f += 1

    return divisors


def d(n):
    return sum(proper_divisors(n))


def is_amicable(m, n):
    return d(m) == n


def solution(i):
    amicables = set()
    for n in range(i+1):
        m = d(n)
        if m != n and is_amicable(m, n):
            amicables.add(m)
            amicables.add(n)
            
    print(amicables)
    return sum(amicables)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(10000))
    # unittest.main()
