import unittest
from math import lcm, gcd, prod


def digs(n):
    return [int(c) for c in str(n)]


def common_digs(numo, deno):
    return list(set(digs(numo)).intersection(set(digs(deno))))


def simplify(numo, deno):
    return numo // gcd(numo, deno), deno // gcd(numo, deno)


def cancelled(n, digs_common, position):
    cancelled_num = ''.join([c for i, c in enumerate(str(n)) if int(c) not in digs_common and i in position])
    cancelled_num = int(cancelled_num) if cancelled_num != '' else 0
    return cancelled_num


def cancelled_simplify(numo, deno):
    digs_common = common_digs(numo, deno)
    return cancelled(numo, digs_common, [0, 1]), cancelled(deno, digs_common, [0, 1])
        

def solution():
    curious_denos = []
    curious_numos = []
    for deno in range(99, 10, -1):
        for numo in range(deno - 1, 9, -1):
            common_digits = common_digs(numo, deno)
            if len(common_digits) == 1:
                if common_digits[0] == 0:
                    continue
                cancelled_numo, cancelled_deno = cancelled_simplify(numo, deno)
                simple_numo, simple_deno = simplify(numo, deno)
                if cancelled_deno == 0:
                    continue
                if cancelled_numo / cancelled_deno == simple_numo / simple_deno:
                    curious_denos.append(cancelled_deno)
                    curious_numos.append(cancelled_numo)
                    print(numo, deno, cancelled_numo, cancelled_deno, simple_numo, simple_deno)
    
    print(curious_numos, curious_denos)
    assert(len(curious_denos) == 4)
    return prod(curious_denos) // gcd(prod(curious_numos), prod(curious_denos))


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution())
    # unittest.main()


""" approach
for a given denominator
generate all fractions less than 1 for that denominator
simplify the fraction and check if it differs from the original by a single digit (two instances)
complexify the fraction, if any complex form fits the curious definition, store it, otherwise stop when you reach the original fraction
multiply four fractions in their simplified forms, return the denominator 
"""

""" pseudocode
curious_product = 1
curious_denos = []
curious_numos = []
for deno in range(99, 10, -1):
 for numo in range(deno-1, 9, -1):
  common_digits = common_digs(numo,deno)
  if len(common_digits) > 0:
   cancelled_numo, cancelled_deno = cancelled_simplify(numo,deno)
   simple_numo, simple_deno = simplify(numo,deno)
   if cancelled_numo / cancelled_deno == simple_numo / simple_deno and (cancelled_numo, cancelled_deno) != (simple_numo, simple_deno):
    # curious found...
    curious_denos.append(simple_deno)
    curious_numos.append(simple_numo)

return lcm(curious_denos)

"""
