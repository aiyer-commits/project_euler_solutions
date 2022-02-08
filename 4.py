import unittest


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


""" pseudocode
max product of three digits = max_three_digit**2
max digits of max product >= length of longest palindrome product
given max digits.. generate palindromes starting from 9999... down


def is_palindrome(s)

while s:
if s[-1] == s[0]: remove i:-1,0, continue
else return false

return true


def max_palprod(n)
max_num = int(n*'9')
max_prod = str(max_num**2)

while !is_palindrome(max_prod)
make next smallest palindrome...
get the square root of the smaller palindrome
if the square root is an integer (floor == float), return smaller palindrome


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


def solution():

    return


if __name__ == "__main__":
    unittest.main()
    print(solution())
