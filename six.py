import unittest


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(2,4),(3,22),(10,2640)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


""" pseudocode

sos = 0
sqs = 0

for i in range(1,n+1)
sos += i**2
sqs += i

sqs = sqs**2

return sqs - sos

"""


def solution(n):
    sos, sqs = 0, 0
    i = 1
    while i < n+1:
        sos += i**2
        sqs += i
        i += 1
    sqs = sqs**2
    
    return sqs - sos


if __name__ == "__main__":
    print(solution(100))
    unittest.main()
    
