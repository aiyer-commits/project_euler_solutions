import unittest


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


""" pseudocode
for all of the values from 100 to 999, calculate products and check if palindrome...

1000^n time
"""


def is_pal(s):
    s = list(s)
    while len(s) > 1:
        if s[-1] == s[0]:
            s.pop()
            s.pop(0)
            continue
        else:
            return False
    return True


def solution():

    maxx = 1

    for i in range(100, 1000):
        for j in range(100, 1000):
            prodd = i*j
            if is_pal(str(prodd)) and prodd > maxx:
                maxx = prodd
    
    return maxx


if __name__ == "__main__":
    #unittest.main()
    print(solution())
