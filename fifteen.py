import unittest

""" approach
fill a grid with path counts starting from 
1x1 up to n+1 x n+1   
"""

""" pseudocode
given n >= 1
start at 1
make a grid n+1 x n+1, fill the boundary with 1s
go column by column, filling each space with
the sum of the value below and to the right.

"""


def solution(n):
    grid = [([0]*n) + [1] for i in range(n)]
    grid.append([1]*(n+1))
    p = (n-1, n-1)
    
    while p != (0, 0):
        r, c = p
        
        grid[r][c] = grid[r+1][c] + grid[r][c+1]
        if c - 1 >= 0:
            p = (r, c-1)
        else:
            p = (r-1, n-1)
        
    grid[0][0] = grid[0][1] + grid[1][0]
    return grid[0][0]


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(2, 6)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(20))
    unittest.main()
