import unittest


def solution(bounds):
    n, m = bounds
    distinct_powers = set()
    for a in range(n, m+1):
        for b in range(n, m+1):
            distinct_powers.add(a**b)
    return len(distinct_powers)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [([2, 5], 15)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution([2, 100]))
    unittest.main()


""" approach
generate all powers a**b, store in set, return set
"""

""" pseudocode

for a in range:
 for b in range:
  set.add(a^b)

return len(set)

"""
