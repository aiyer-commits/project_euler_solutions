import unittest


def frac_cycle_length(denom):
    quotients = {}
    numera = 1
    cycle_length = 0
    while numera != 0:
        cycle_length += 1
        numera *= 10
        if numera not in quotients:
            quotients[numera] = cycle_length
        else:
            print(quotients)
            print(cycle_length - quotients[numera])
            return cycle_length - quotients[numera]

        numera = numera % denom

    return 0


def solution(end):
    longest_length = 0
    d_longest = -1
    for d in range(2, end+1):
        length_d = frac_cycle_length(d)
        if length_d > longest_length:
            longest_length = d
            d_longest = d
            
    return d_longest


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(10, 7)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return

    
if __name__ == "__main__":
    # print(solution(999))
    frac_cycle_length(7)
    frac_cycle_length(983)
    # unittest.main()


""" approach
cycle finding using a hashmap and cycle length pointer
"""

""" pseudocode
no pseudocode because i used this link to solve this:

https://helloacm.com/computing-the-longest-recurring-cycle-in-its-decimal-fraction-part/
"""
