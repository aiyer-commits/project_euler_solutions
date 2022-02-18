import unittest

""" approach
generate grid, start 0,0, target n-1,n-1
bfs, increment valid paths count when point = target
  
"""

""" pseudocode
n <- grid size

def in_bounds(p):
x,y = p
return 0 < x < n and 0 < y < n

def translate(p,t)
x,y = p
tx,ty = t
return (x + tx, y + ty)

translations = [(0,1),(1,0)]

valid_paths = 0

stack = [(0,0)]
while stack:
point = stack.pop()
if point == (n-1,n-1):
valid_paths += 1
continue
stack.extend([translate(point,t) for t in translations if in_bounds(translate(point,t))])





"""


def solution(n):
    def in_bounds(p):
        x, y = p
        return 0 <= x <= n and 0 <= y <= n

    def translate(p, t):
        x, y = p
        tx, ty = t
        return (x + tx, y + ty)

    valid_paths = 0
    translations = [(0, 1), (1, 0)]

    stack = [(0, 0)]

    while stack:
        point = stack.pop()
        if point == (n, n):
            valid_paths += 1
            continue
        stack.extend(
            [
                translate(point, t)
                for t in translations
                if in_bounds(translate(point, t))
            ]
        )

    return valid_paths


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(2, 6)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    solution(20)
    unittest.main()
