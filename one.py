import unittest

"""
sum of alls multiple of 3 or 5 below n

a multiple is 3*p or 5*p...
so you need all of the primes to do it?

what about in reverse...
divide out 3 and 5 from n, move by remainder downward...
if no remainder... jump by divisor down until you get to zero...
but be careful to not double count...

sum = 0
while n > 0:
if (n % 3 == 0 and n % 5 == 0) or (n % 3 == 0): sum += n, n -= 3
elif n % 5 == 0: sum += n, n -= 3
else: n -= n % 5

return sum




"""


def sum_of_multiples(factors: list, n: int) -> int:
    factors.sort()
    summ = 0
    n -= 1
    while n > 0:
        if (
            (n % factors[0] == 0 and n % factors[-1] == 0)
            or (n % factors[0] == 0)
            or (n % factors[-1] == 0)
        ):
            summ += n
        rems = [f if n % f == 0 else n % f for f in factors]
        min_rem = min(rems)
        n -= min_rem
    return summ


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [([3, 5], 10, 23)]
        for factors, n, summ in cases:
            self.assertEqual(sum_of_multiples(factors, n), summ)
        return


if __name__ == "__main__":
    # unittest.main()
    print(sum_of_multiples([3, 5], 1000))
