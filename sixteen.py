import unittest

""" approach
cheesed because python doesn't have overflow

"""

""" pseudocode

"""


def solution(n):
    return sum([int(c) for c in str(2**n)])


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(15, 26)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1000))
    unittest.main()
