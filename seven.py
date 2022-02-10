import unittest


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(0, 1), (1, 2), (3, 5), (6, 13)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


""" pseudocode


f = [1,2]

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
if n == 0 return n
if n < len(f):
return f[n-1]

q = f[-1]
while len(f) < n:
if is_prime(q) 
f.append(q)

return f[n-1]

"""

f = [1, 2]


def is_prime(m):
    o = 1
    while o < len(f) and m != f[0]:
        if m % f[o] == 0:
            return False
        else:
            o += 1

    return True


def get_prime(n):
    if n == 0:
        return 1
    if n < len(f) + 1:
        return f[n]

    q = f[-1]
    while len(f) < n + 1:
        if is_prime(q):
            f.append(q)
        else:
            q += 1

    return f[n]


def solution(n):
    return get_prime(n)


if __name__ == "__main__":
    print(solution(10001))
    unittest.main()
    
