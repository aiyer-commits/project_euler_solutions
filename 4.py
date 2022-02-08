import unittest


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(9999, 9009)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


""" pseudocode
max product of three digits = max_three_digit**2
max digits of max product >= length of longest palindrome product
given max digits.. generate palindromes starting from 9999... down


def is_palindrome(s,i=0)
isnt = i
s = s[i:i-1]
while s:
if s[0] == s[-1]: remove 0,-1,0, isnt += 1 continue
else return isnt

return -1

def get_palindrome(s):
sub = 0
while is_palindrome(s) == -1:
if s[sub] == 0:
sub -= 1
else:
s[sub] -= 1
s[-sub] = s_sub

 

what about...
generate palindrome
do prime factorization...
reduce prime factors to two factors...
if len each of two factors is n, then success
else, generate palindrome...
 
"""


def trial_division(n):
    stack = []
    f = 2
    while n > 1:
        if n % f == 0:
            stack.append(f)
            n //= f
        else:
            f += 1
    return stack


def next_pal(p):
    sub = len(str(p)) // 2
    found = False
    p = list(str(p))
    while not found:
        if p[sub] > 0:
            p[sub] -= 1
            p[-sub] = p[sub]
            found = True
        else:
            p[sub], p[-sub] = 9, 9
            sub -= 1
    return int(str(p))


def biggest_composite_factors(factors, d):
    composite = 1
    len_d_factors = []
    while factors:
        f = factors.pop()
        composite *= f
        if len(str(composite)) == d and len(str(prod(factors))) == d:
            return [composite, prod(factors)]
        elif len(str(composite)) > d:
            composite /= f
            factors.insert(0, composite)
            composite = f
    return []


def solution(p):

    return


if __name__ == "__main__":
    unittest.main()
    print(solution())
