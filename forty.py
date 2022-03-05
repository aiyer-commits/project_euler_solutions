import unittest
from math import prod


def solution(indices):
    digs_at_indices = []
    curr_index = 1
    num = 1
    indices.sort()
    for i in indices:
        while curr_index < i:
            num += 1
            curr_index += len(str(num))
        print(num, curr_index)
        offset = len(str(num)) - (curr_index - i)
        digs_at_indices.append(int(str(num)[offset-1]))
    print(digs_at_indices)
    return prod(digs_at_indices)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(list(range(1, 4)), 6), (list(range(1, 10)), 362880)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution([1, 10, 100, 1000, 10000, 100000, 1000000]))
    unittest.main()


""" approach
the each index occurs within a certain range of concatenated numbers...
the first nine indices occur in the numbers less than 10
the first 99 indices occur in the numbers less than 100... 

the index of a particular digit in relation to the numbers in the constant is relative to the number of digits in each of the numbers....

numbers 1-9 contribute 1 digit
10-99, two digits
100-999, three digits
1000-9999, four digits...

the number of numbers of a given digit length are 10^n - 1 - 10^n-1, where n is the the number of digits in a number... 

there must be a way to describe the relationship between an index and the digit at that index...

numbers 1:9, indices 1:9
numbers 10:99, indices 10:2*(89)
numbers 100:999, indices 2*(89)+1:3*899

n:100 , i: 1*(10-1) + 2*(10^2-1-10) -> index 187...


log base 10 of the desired index...? 

other way to do it is to just keep adding numbers and generating a current index.. until you've hit all indices in a desired set of indices... 


"""

""" pseudocode

sol(indices):
digs_at_indices = []
curr_index = 1
num = 1
indices.sort()
for i in indices:
 while curr_index < i:
  num += 1
  curr_index += len(str(num))
 digs_at_index.append(int(str(num)[curr_index - i]))

return prod(digs_at_index)
"""
