import unittest

""" approach
search for values of a,b,c that satisfy the three constraints
"""

""" pseudocode
n = 12
a_b = 2
max_ab = n - a_b
while a_b < max_ab
c = n - a_b
a = a_b // 2
b = a_b - a
if b != a and a^2 + b^2 == c^2 
return a*b*c
a_b += 1

return -1


"""


def is_pythag_trip(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def solution(n):

    a_b = 2
    max_ab = n - a_b

    while a_b < max_ab:
        c = n - a_b
        a = a_b // 2
        b = a_b - a
        if b == a:
            while a > 2:
                a -= 1
                b += 1
                if is_pythag_trip(a, b, c):
                    return a * b * c
        elif is_pythag_trip(a, b, c):
            return a * b * c
        a_b += 1

    return -1


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(12, 60)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1000))
    unittest.main()
