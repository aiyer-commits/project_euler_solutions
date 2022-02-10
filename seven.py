import unittest


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


""" pseudocode


f = [2]

is_prime(m)
s = []
o = 0
while m > 1 and len(s) < 1 and o < len(f) and m != f[o]:
if m % f[o] == 0:
s.append(f[o])
m //= f[o]
else:
o += 1
if len(s) > 0: return False
else: return True


get_prime(n):
for q in range(n+1):
if is_prime(q)
f.append(q)

return f[-1]

"""


def solution():

    return


if __name__ == "__main__":
    unittest.main()
    print(solution())
