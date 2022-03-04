import unittest
from math import sqrt


def hypot(a, b):
    return sqrt(a**2 + b**2)


def perim(a, b, c):
    return sum([a, b, c])


def solution(p):
    perims = {}
    for a in range(1, p):
        for b in range(a, p):
            if a + b > p:
                continue
            c = hypot(a, b)
            if c - int(c) == 0:
                pp = perim(a, b, int(c))
                if pp <= p:
                    if pp in perims:
                        perims[pp].add((a, b, c))
                    else:
                        perims[pp] = set([(a, b, c)])
    max_sols = 0
    pp_max = 0
    for pp in perims:
        sols = len(perims[pp])
        if sols > max_sols:
            max_sols = sols
            pp_max = pp
            
    return pp_max


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1000))
    # unittest.main()


""" approach
iterate through a,b,c, generating c using pythagorean theorem... 
check if a,b, and c sum to less than p
for each p, store a set of tuples containing solutions
return the p with the greatest number of solutions...
safe upper boundary is 999, but 500 is probably good enough 
"""

""" pseudocode
def hypot(a,b):
  return sqrt(a**2 + b**2)

def perim(a,b,c):
  return a + b + c

def sol(p):
 perims = {}
 for a in range(1,p):
  for b in range(a,p):
   c = hypot(a,b)
   pp = perim(a,b,int(c))
   if c - int(c) == 0 and pp <= p:
    if pp in perims:
     perims[pp].add((a,b,c))
    else:
     perims[pp] = set([(a,b,c)])
 longest = 0
 p_max = 0
 for pp in perims:
  num_sols = len(perims[pp])
  if num_sols > longest:
   longest = num_sols
   p_max = pp

 return p_max
"""
