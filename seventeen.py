import unittest

""" approach
for n < 1000
there are three 'depths' of numbers
single digit, double digit, triple digit...
in single digit form, there are nine words total...
in double digit form, there are 9 words representing the teens, and 9 words representing the multiples of ten < hundred
in triple digit form, the hundreds place is simply the single digit form and the word hundred
 the tens/ones place comes with an additional 'and' (3 chars) because of the writing style (British)

if you have the count of each of these forms, and you sum them, then you have the total number of words...

onetwothreefourfivesixseveneightnine = 37
teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen = 71
twentythirtyfourtyfiftysixtyseventyeightyninety = 48
hundred = 7
and = 3
thousand = 8

range(1,10) = 37
range(10,100) = 71 + (48 + 37) * 9
range(100,1001) = 37*7 + 71 + (48 + 37)*9 + 3*(900) - 10 + 37*9 + (3 + 8) 

this approach *should* work, but its ugly and the assumption here are n is 1000...
the generator approach might take longer but will be easier to generalize..
"""

""" pseudocode
given a number n in decimal form
convert to string, count the length.. this set the upper bound of representations.. (thousand, hundred, ten, one)
given a length... can calculate the number of forms for each length-1, ... , 0.
len(ones) + len(tens) + len(hundreds)
"""


def solution():

    return


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    # print(solution())
    unittest.main()
