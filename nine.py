import unittest
from random import randint
from math import prod

""" approach
random search...

given n
get a random number less than n -> r0
subtract r0 from n -> upper_bound
get a random number less than upper_bound -> r1
upper_bound - r1 -> r2

test if r0,1,2 are a pythagorean triple...
continue until you've found one.... 

"""

""" pseudocode

is_pythag(a,b,c)
return a^2 + b^2 == c^2


trial_and_error (n)

while true
r0 = rand(2 < r < n-2)
upper_bound = n - r0
r1 = rand(1,upper_bound)
r2 = upper_bound - r1
if r1 != r2 != r3:
perms = permutations([r0,r1,r2])
for p in perms
is_pythag(p)
return r0*r1*r2

wow, interesting

"""


def is_pythag(p):
    return p[0] ** 2 + p[1] ** 2 == p[2] ** 2


at_least_one_solution_exists = True


def solution(n):

    while at_least_one_solution_exists:
        r0 = randint(3, n - 3)
        ub = n - r0
        r1 = randint(1, ub)
        r2 = ub - r1
        if r0 != r1 != r2 and is_pythag([r0, r1, r2]):
            print([r0, r1, r2])
            return prod([r0, r1, r2])


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(12, 60)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1000))
    unittest.main()
