import unittest

""" approach
subtract the years in the range...
subtract the months...
subtract the days...

what defines a sunday that's a first of the month?
two kinds of years:
leap, non-leap
7 days a week,
1900 jan 1 is a monday...call monday day 0 of the week
in 365 days...12 first of months
52 weeks... 52 sundays at most
how many first of months are also sundays...

non-leap year starts on monday, next year starts on sunday (+1)
leap year starts on monday, next year starts on saturday (+2)
                                                                                                                                                         
day of the first of the month in a leap year: [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
day of the first of the month in a non leap year: [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]

each year... the day representing sunday increase by the remainder of number of days in the year % days in a week

so in 1900 which is not a leap year, monday is day 0, sunday is day 6, in range day 0 - 6
in 1901, sunday is day 0
1902: day 1
03: 2
04: 3
05: 5!!
06: 6
07: 0
08: 2

just sum the number of times that day occurs as the first day of the month for a given year (leap/non-leap)


"""

""" pseudocode



"""


def is_leap(y):
    if (y % 100 == 0 and y % 400 == 0 and y % 4 == 0) or (y % 100 != 0 and y % 4 == 0):
        return True
    else:
        return False


def solution(range_and_sunday_index):
    start_year, end_year, sunday_index = range_and_sunday_index
    num_sundays = 0
    dfoml = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
    dfom = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]

    for y in range(start_year, end_year + 1):
        if is_leap(y):
            num_sundays += dfoml.count(sunday_index)
            sunday_index = (sunday_index - 2) % 7
        else:
            num_sundays += dfom.count(sunday_index)
            sunday_index = (sunday_index - 1) % 7

    return num_sundays


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [((1900, 1900, 6), 2)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution((1901, 2000, 0)))
    unittest.main()
