import unittest


def sieve(n):
    primes = []
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, n+1, i))
    return primes


def digs(n):
    return [int(c) for c in str(n)]


def int_from_digits(digits):
    return int(''.join([str(i) for i in digits]))


def rots(n):
    rotations = [n]
    digits = digs(n)
    num_rots = len(digits) - 1
    curr_rot = 0
    while curr_rot < num_rots:
        end = digits.pop()
        digits.insert(0, end)
        rotations.append(int_from_digits(digits))
        curr_rot += 1
    return rotations


def solution(n):
    primes = sieve(n)
    circular = set()
    while primes:
        p = primes[0]
        valid = True
        for n in rots(p):
            if n not in primes:
                primes.remove(p)
                valid = False
                break
        if valid:
            for n in rots(p):
                if n in primes:
                    primes.remove(n)
                    circular.add(n)
    return len(circular)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(100, 13)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(1000000))
    unittest.main()


""" approach
generate all primes less than 1 million
iterate through them, generate all rotations, check if all rotations are in the set of primes
if yes, add to list

return list of circular primes
"""

""" pseudocode
sieve(n) -> primes
rotations(n) -> [rotations]
sol(n):
 while primes:
   p = primes[0]
   for n in rotations(p)
     if n not in primes:
       primes.remove(p)
       break
   circular.append(p)
   circular.extend(rotations(p))
   for n in rotations(p):
    primes.remove(n)
 return len(circular)

"""
