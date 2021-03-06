import unittest


def pentagonal(n):
    return (n * (3 * n - 1)) / 2


def solution():
    no_solution = True
    pentagonals = [1.0, 5.0, 12.0]
    smallest = float('inf')
    n = 3
    while no_solution:
        p_l = pentagonals[-1]
        for p_i in pentagonals[:-3]:
            p_j = (p_l - p_i) / 2
            if p_j in pentagonals:
                p_k = (p_l + p_i) / 2
                if p_k in pentagonals:
                    print('p_j', p_j)
                    print('p_k', p_k)
                    print('p_i', p_i)
                    print('p_l', p_l)
                    if p_i < smallest:
                        smallest = p_i
                    else:
                        no_solution = False
        n += 1
        pentagonals.append(pentagonal(n))
    return smallest


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution())
    # unittest.main()


""" problem
Pentagonal numbers are generated by the formula, Pn=n(3nā1)/2. The first ten pentagonal numbers are:



1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...



It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 ā 22 = 48, is not pentagonal.



Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk ā Pj| is minimised; what is the value of D?
"""


""" approach
the difference between two consecutive pentagonal numbers only increases...
the satisfying pair can't be found simply by subtracting consecutive pairs...

there is a system of equations that satisfy the requirement

Pk - Pj = Pi
Pj + Pk = Pl
Pk > Pj
Pl > Pi

Pi = -(Pl - Pk) + Pk = 2Pk - Pl
Pl = Pk - Pi + Pk = 2Pk - Pi

Pi = Pl - 2Pj
Pl = Pi + 2Pj

Pk = (Pi + Pl) / 2
Pj = (Pl - Pi) / 2

given this last set of equations... can search for pairs of pi and pl that generate
pk and pj... n*log(n) where n is the set of pentagonal numbers... 

is there a way to eliminate a subset of pentagonal numbers?
or do you have to n*n-1/2 comparisons?
seems necessary

what is the termination condition?
we want the smallest Pi, if Pi's increase monotonically then the first time we meet
a larger Pi than the previous, we can terminate...

"""

""" pseudocode
pentagonal(n) -> int
return (n*(3*n - 1))/ 2

sol()
pentagonals = [1, 5, 12]
i = len(pentagonals) - 1
diff = float('inf')
no_solution = True
n = 3
while no_solution:
 p_l = pentagonals[i]
 for p_i in pentagonals[:i - 2]:
  p_j = (p_l - p_i) / 2
  if p_j in pentagonals:
   p_k = (p_l + p_i) / 2
   if p_k in pentagonals:
     if p_i < diff:
      diff = p_i
     else:
      no_solution = False
 n += 1
 pentagonals.append(pentagonal(n))

"""
