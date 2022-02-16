import unittest

""" approach
a + b + sqrt(a**2 + b**2) = 1000

"""

""" pseudocode
a = 1
b = n - a - sqrt(a**2 + b**2)

"""


def solution(n):



class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(12, 60)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1000))
    unittest.main()
