import unittest

""" approach

"""

""" pseudocode

"""


def solution(n):
    f = 1
    for m in range(1, n + 1):
        f *= m
    return sum([int(c) for c in list(str(f))])


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(10, 27)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(100))
    unittest.main()
