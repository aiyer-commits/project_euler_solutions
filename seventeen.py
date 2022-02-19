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

this approach above does not produce the answer...
the generator approach below does work however..
and should work up to 9999
"""

""" pseudocode
given a number n in decimal form

"""

l_20 = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
tens = [
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
andd = "and"
hundred = "hundred"
thousand = "thousand"


def rep(m):
    len_m = len(m)
    if int(m[0]) == 0 and len_m > 1:
        return rep(m[1:])
    if len_m == 4:
        prefix = l_20[int(m[0]) - 1]
        return prefix + thousand + rep(m[1:])
    elif len_m == 3:
        if int(m[1]) == 0 and int(m[2]) == 0:
            return l_20[int(m[0]) - 1] + hundred
        return l_20[int(m[0]) - 1] + hundred + andd + rep(m[1:])
    elif len_m == 2:
        if int(m[0]) == 1:
            return l_20[10 + int(m[1]) - 1]
        else:
            return tens[int(m[0]) - 1] + rep(m[1:])
    elif len_m == 1:
        if int(m[0]) == 0:
            return ""
        return l_20[int(m[0]) - 1]
    else:
        return ""


def solution(n):
    letters = ""
    for m in range(1, n + 1):
        r = rep(str(m))
        letters += r
    return len(letters)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(5, 19)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(rep('9999'))
    print(solution(1000))
    unittest.main()
