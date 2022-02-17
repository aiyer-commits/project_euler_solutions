import unittest

""" approach

"""

""" pseudocode



"""


def solution(n):
    m = n
    longest_seq = 0
    lsm = m
    while m > 1:
        p = m
        seq = 0
        while p != 1:
            if seq > longest_seq:
                longest_seq = seq
                lsm = m
            seq += 1
            p = p / 2 if p % 2 == 0 else 3*p + 1
        m -= 1
        
    return lsm


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(9, 9)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1000000))
    unittest.main()
