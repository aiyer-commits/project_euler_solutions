import unittest


def num_to_digs(n):
    return [int(c) for c in str(n)]


def digs_expo_sum(digs, expo):
    expo_sum = 0
    for d in digs:
        expo_sum += d ** expo
    return expo_sum


def digs_expo_sum_equals(digs, expo, bound):
    expo_sum = 0
    for d in digs:
        expo_sum += d ** expo
        if expo_sum > bound:
            return False
        elif expo_sum == bound:
            return True
    return True


def solution(d):
    valid_terms_sum = 0
    valid_terms = []
    n = 2
    while n < 2 ** 20:
        if digs_expo_sum(num_to_digs(n), d) == n:
            valid_terms.append(n)
            valid_terms_sum += n
        n += 1
    print(valid_terms)
    return valid_terms_sum


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(4, 19316)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    # print(solution(2))
    # print(solution(3))
    print(solution(5))
    unittest.main()


""" approach
generate all numbers in range 10^n - 10^n-1
break each number into its digits, apply formula and check equivalence

no upper bound defined!! danger...
permutations should not be tested either...

"""

""" pseudocode

num_to_digs -> [digits]

digs_expo_sum(digits,expo) -> expo_sum
 expo_sum = 0
 for d in digits
   expo_sum += d**expo
 return expo_sum

d <- number of digits
range <- 10^d-1, 10^d
summ <- 0
valid_terms = []
for n in range
 if digs_expo_sum == n:
   summ += digs_expo_sum
   valid_terms.append(n)
print(valid_terms)
return summ

"""
