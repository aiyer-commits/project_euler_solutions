import unittest
from itertools import permutations


def all_substrings(n):
    s = str(n)
    return [int(s[i : i + 3]) for i in range(1, len(s) - 2)]


def divisible(n):
    substrings = all_substrings(n)
    factors = [2, 3, 5, 7, 11, 13, 17]
    divisible = [s % f == 0 for s, f in zip(substrings, factors)]
    return all(divisible)


def int_from_list(listt):
    return int(''.join([str(i) for i in listt]))


def all_pandigitals(n):
    non_zero_digits = [i for i in range(1, n + 1)]
    pandigitals = []
    for index, digit in enumerate(non_zero_digits):
        all_other_digits = non_zero_digits[:index] + non_zero_digits[:index:-1] + [0]
        pandigitals.extend(
            [
                int_from_list([digit] + list(permutation))
                for permutation in list(permutations(all_other_digits))
            ]
        )
    return pandigitals


def solution():
    sum_of_divisibles = 0
    pandigitals = all_pandigitals(9)
    for pd in pandigitals:
        if divisible(pd):
            sum_of_divisibles += pd
            print(pd)
    return sum_of_divisibles


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution())
    unittest.main()


""" problem
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.



Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:



d2d3d4=406 is divisible by 2

d3d4d5=063 is divisible by 3

d4d5d6=635 is divisible by 5

d5d6d7=357 is divisible by 7

d6d7d8=572 is divisible by 11

d7d8d9=728 is divisible by 13

d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""


""" approach
generate all 0-9 pandigital numbers (9*9!, assuming 0 cannot be the first digit...)
test each one for substring divisibility for the primes in range 2-17
sum each of the divisible numbers
"""

""" pseudocode
substrings(n)->[int)
s = str(n)
return [int(s[i:i+3]) for i in range(1,len(s)-2)]

divisible(n):
substring = substrings(n)
factors = [2, 3, 5, 7, 11, 13, 17]
divisible = [s % f == 0 for (s, f) in zip(substrings,factors)]
return all(divisible)

from itertools import permutations

all_pandigitals(n):
non_zero_digits = [i for i in range(1, n+1)]
pandigitals = []
for index, digit in enum(non_zero_digits):
 all_other_digits = non_zero_digits[:index] + non_zero_digits[:index:-1] + [0]
 pandigitals.extend([[digit] + permutation for permutation in list(permutations(all_other_digits))])
return pandigitals

sol()
sum_of_divisibles = 0
all_pandigitals = all_pandigitals(9)
for pd in all_pandigitals:
 if divisible(pd):
  sum_of_divisibles += pd
return sum_of_divisibles

"""
