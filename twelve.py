import unittest

""" approach

def factors(n)
d = 2
f = [1]
while n > 1:
 if n % d == 0:
 n //= d
 f.append(d)
d += 1
return f

solution(n):

num_factors = 0
triangle_number = 0
i = 1

while num_factors < n
triangle_number += i
i += 1
num_factors = len(factors(triangle_number))

return triangle_number

"""

""" pseudocode

"""


def factors(n):
    d = 2
    f = set([1])
    while d <= n:
        if n % d == 0:
            f.add(d)
        d += 1
    return f


def solution(n):
    num_factors = 0
    triangle_number = 0
    i = 1
    max_num_factors = 0
    while num_factors < n:
        triangle_number += i
        i += 1
        num_factors = len(factors(triangle_number))
        if num_factors > max_num_factors:
            max_num_factors = num_factors
            print(triangle_number, i, num_factors)
    return triangle_number


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(1, 1), (6, 28)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(500))
    unittest.main()
