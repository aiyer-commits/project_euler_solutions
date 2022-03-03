import unittest


def is_pal(st):
    s = list(st)
    while len(s) > 1:
        if s[0] == s[-1]:
            s.pop()
            s.pop(0)
        else:
            return False
    return True


def solution(n):
    summ = 0
    for i in range(1, n + 1):
        deci = str(i)
        bina = format(i, 'b')
        if is_pal(bina) and is_pal(deci):
            summ += i
            
    return summ


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(10, 1+3+5+7+9)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1000000))
    unittest.main()


""" approach
couple of ways to go about this...
could generate all palindromes, or could check all values in range...
check all values in range is less efficient, but easier to validate
"""

""" pseudocode
is_pal(s) -> Bool
while s:
 if s[0] == s[-1]
  pop, remove
 else return False
return True

sol(n):
summ = 0
for i in range(1,n+1):
 deci = str(i)
 bina = format(i, 'b')
 if is_pal(bina) and is_pal(deci):
  summ += i

return summ

"""
