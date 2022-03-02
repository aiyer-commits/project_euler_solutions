import unittest


def change_ways(target, summands):
    known_ways = [0] * (target + 1)
    known_ways[0] = 1
    for i in range(len(summands)):
        for j in range(summands[i], target + 1):
            known_ways[j] += known_ways[j - summands[i]]
    return known_ways[-1]


def solution(case):
    target, summands = case
    return change_ways(target, summands)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [((1, (1, 2, 5)), 1), ((2, (1, 2, 5)), 2), ((3, (1, 2, 5)), 2), ((4, (1, 2, 5)), 3), ((5, (1, 2, 5)), 4), ((6, (1, 2, 5)), 5)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution((200, (1, 2, 5, 10, 20, 50, 100, 200))))
    unittest.main()


""" approach
dynamic programming...
greedy, given target sum... subtract largest summand, and then recursively solve for all summands smaller than the remaining amount...

t: 5, s: 1,2,5

1,1,1,1,1
1,1,1,2
1,2,2
5



"""

""" pseudocode
sol(t,s):
s.sorted()
return change_ways(t,s)

change_ways(t,s):
ways = 0
r <- t
for c in s:
 u <- r - c
 if u > 0:
  ways += change_ways(u,s)
 elif u == 0:
  ways += 1
   

return ways

"""
