import unittest


alphabet = list('abcdefghijklmnopqrstuvwxyz')
alphahash = {c: i for i, c in enumerate(alphabet, 1)}


def name_score(s):
    s = s.strip('\"')
    score = 0
    for c in s:
        # score += alphabet.index(c) + 1 # could be sped up with a hashmap
        if c.isalnum():
            score += alphahash[c.lower()]
    return score


def solution(file):
    names = sorted(open(file).read().split(','))
    total = 0
    for index, name in enumerate(names, 1):
        #print(index, name_score(name))
        total += index * name_score(name)
    
    return total


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [('./arjun.txt', 3*(1+18+10+21+14))]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution('./p022_names.txt'))
    unittest.main()


""" approach
open the file, store all lines in an arry
sort the array alphabetically
iterater through the array, calculating name score
sum the name scores as you iterate
return the name score
"""

""" pseudocode
name_score(s):
alphabet = [...] #0,25
score = 0
for c in s:
score += alphabet.index(c) + 1
return score

solution(file):
names = open(file).read().split('\n')
names.sort()
names_sum = 0
for index,name in enumerated(names):
names_sum += (index+1)*name_score(name)

return names_sum

"""
