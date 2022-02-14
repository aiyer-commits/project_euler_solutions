import unittest

""" approach
a**2 +  b**2  + 0 = c**2
a + b - 1000 = c

a**2 + b**2 = (a + b - 1000)**2
a**2 + b**2 = a**2 + ab - 1000a + ba + b**2 - 1000b + 1000a + 1000b + 1000**2
a**2 + b**2 = a**2 + 2ab + b**2 + 1000**2
0 = 2ab + 1000**2
-1000**2 / 2 = ab
-500000 = ab5
a = -500000/b

-500000/b + b - 1000 = c
-500000b**2/b - 1000 = c
b = (c + 1000)/-500000

-500000 * (-500000b^2/b - 1000) = abc
(50000**2)(b**2)/b + 500000000 = abc



"""

""" pseudocode

"""


def solution():

    return


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    # print(solution())
    unittest.main()
