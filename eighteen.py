import unittest

""" approach
find the maximum for a given node by summing it with each of its children and comapring the two sums
store the bigger sum at that node and continue up, this is dynamic programming
"""

""" pseudocode
t := triangle graph
h := height of triangle
for r in range(h-2,-1,-1):
for c in range(0,r+1):
t[r][c] = max(t[r+1][c] + t[r][c], t[r+1][c+1] + t[r][c])

return t[0][0]


"""
t0 = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3],
] # answer: 23

t1 = [
    [3],
    [7, 4],
    [2, 4, 8],
    [8, 5, 9, 3],
] # answer: 24


t2 = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]


def solution(t):
    h = len(t)
    
    for r in range(h-2, -1, -1):
        for c in range(0, r+1):
            t[r][c] = max(t[r+1][c] + t[r][c], t[r+1][c+1] + t[r][c])
        
    return t[0][0]


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(t0, 23), (t1, 24)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(t2))
    unittest.main()
