import unittest


def solution(n):
    corner_square = 2
    if n % 2 != 0:
        corner_square = 3
    diag_sum = 1
    curr_corner = 1
    while corner_square <= n:
        final_corner = corner_square ** 2
        corner_dist = corner_square - 1
        while curr_corner < final_corner:
            curr_corner += corner_dist
            diag_sum += curr_corner
        corner_square += 2
        
    return diag_sum


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(5, 101), (4, 56), (2, 10)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1001))
    unittest.main()


""" approach
n represents side length, sq number.... but also an odd number... square numbers that are even do not fall on corners... 
can generate the spiral grid as a 2d array, and then traverse the grid.. t: n**2, s: n**2.
or
can directly generate the corners??? by traversing the grid virtually... t: log(n), s: log(n)

each level of the grid is bounded by a square number, sqn: 3**2, 5**2, 7**2... 
each corner can be reached by adding corner distance (cd): sqn - 1... 1 + 2, 3 + 2, 5 + 2... get to sqn, increment sqn number by 2, increment cd by 1

can be expanded to even numbers... 2**2, 4**2

can be done in reverse too... 



"""

""" pseudocode

n <- grid side length

if n % 2 == 0: sqn = 2
else: sqn = 3
diag_sum = 1
curr_corner = 1
while sqn <= n:
 final_corner = sqn ** 2
 corner_dist = sqn - 1
 while curr_corner < final_corner:
  curr_corner += corner_dist
  diag_sum += curr_corner
 sqn += 2

return diag_sum


 
"""
