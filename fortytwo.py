import unittest
from math import sqrt


def calc_word_value(s):
    letter_vals = [ord(c) - 64 for c in s]
    return sum(letter_vals)


def quadratic_root(i):
    return (1 + sqrt(1 + (8 * i))) / 2


def solution():
    count = 0
    with open('./p042_words.txt', 'r') as f:
        words_string = f.read()
        words = [word.strip('"') for word in words_string.split(',')]
        for word in words:
            word_value = calc_word_value(word)
            qr = quadratic_root(word_value)
            if qr == int(qr):
                print(word, word_value, qr)
                count += 1
    return count


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
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:



1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...



By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.



Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""


""" approach
given the formula for a triangle number
the inverse formula is:
2tn = n(n+1)
...

no the inverse won't work
need the quadratic formula

n^2 + n - 2tn = 0

1 + sqrt(1 + 4(2tn)) / 2 (only the positive root can possibly be a solution)

if this number is an integer, we have a triangle number.



"""

""" pseudocode
read file
iterate through words
sum ordinal values of letters in word to generate potential triangle number
calculate triangle number index.
if index is integer, then we have a triangle number, increment count
return count
"""
