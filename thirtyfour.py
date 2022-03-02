import unittest
from math import prod


def fac(n):
    return prod([i for i in range(1, n + 1)])


def digs(n):
    return [int(c) for c in str(n)]


def digs_fac_sum(n):
    return sum([fac(d) for d in digs(n)])


def int_from_list(listt):
    return int(''.join([str(d) for d in listt]))


def find_max_bound():
    max_digs = [9]
    max_bound = int_from_list(max_digs)
    while max_bound < digs_fac_sum(max_bound):
        max_digs.append(9)
        max_bound = int_from_list(max_digs)
    return max_bound


def solution():
    max_bound = find_max_bound()
    n = 10
    digit_factorials = []
    print(max_bound)
    while n < max_bound:
        if digs_fac_sum(n) == n:
            print(n)
            digit_factorials.append(n)
        n += 1
    
    return sum(digit_factorials)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution())
    # unittest.main()


""" approach
starting at 10, there is a maximum bound b > 1, 9!*b where b+1...b+n will always be smaller than [9]*b
while underneath that boundary, test every number to see if it is a digit factorial

"""

""" pseudocode

def fac(n):
 return prod([n for n in range(1+n+1)])

def digs(n):
 return [int(c) for c in str(n)]

def digs_fac_sum(n):
 return sum([fac(d) for d in digs(n)])

def int_from_list(listt):
 return int(''.join([str(d) for d in listt]))

def find_max_bound():
 max_digs = [9]
 max_bound = int_from_list(max_digs)
 while max_bound < fac(max_bound):
  max_digs.append(9)
  max_bound = int_from_list(max_digs)
 return max_bound

def sol():
  max_bound = find_max_bound()
  n = 10
  digit_factorials = []
  while n < max_bound:
   if digs_fac_sum(n) == n:
    digit_factorials.append(n)

  return sum(digit_factorials)

"""
