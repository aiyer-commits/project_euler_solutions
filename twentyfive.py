import unittest


fibs = [1, 1]
index = 2


def fib(n):
    global index
    while index < n:
        fibs.append(fibs[-1] + fibs[-2])
        index += 1
    return fibs[n - 1]


def solution(d):
    if d == 1:
        return 1
    n = 3
    while len(str(fibs[-1])) < d:
        fib(n)
        n += 1
    return len(fibs)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(1, 1), (2, 7), (3, 12)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1000))
    unittest.main()


""" approach
generate fibonacci numbers...
count digits... return first one that is n digits
"""

""" pseudocode
fibs = [1,1]
index = 2
def fib(n):
 while index < n:
  fibs.append(fibs[-1] + fibs[-2])
  index += 1
 return fibs[n-1]


def solution(d):
  if d == 1: return 0
  n = 3
  while len(str(fib[-1])) < d:
   fib(n)
   n += 1
  return len(fibs)

"""
