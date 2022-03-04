import unittest


def digs(n):
    return [c for c in str(n)]


def all_digs_unique(n):
    return len(set(digs(n))) == len(digs(n))


def solution(n):
    i = 1
    dig_prod = ''
    f = 1
    max_dig_prod = 0
    while len(dig_prod) < n + 1:
        prodd = i*f
        if len(set(list(dig_prod)).intersection(set(digs(prodd)))) == 0 and all_digs_unique(prodd) and '0' not in str(prodd):
            dig_prod += str(i*f)
            # print(dig_prod)
            if len(dig_prod) == n:
                if int(dig_prod) > max_dig_prod:
                    max_dig_prod = int(dig_prod)
                    print(max_dig_prod)
                i += 1
                f = 1
                dig_prod = ''
            elif len(dig_prod) < n:
                f += 1
        elif int(dig_prod + str(prodd)) > 5000000000000:
            break    
        else:
            i += 1
            dig_prod = ''
            f = 1
    return max_dig_prod


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution(9))
    # unittest.main()


""" approach
start with a pandigital number,
divide it by two...

or start at 1 and concatenate the first 9 products...

at most you will do 9 products...

is the upper bound defined by the first number whose multiple results in a n + 1 digit digital product? Could be....

"""

""" pseudocode
digs(n) -> [str(digs)]
all_digs_unique -> Bool

sol(n):
 i = 1
 dig_prod = ''
 f = 1
 max_dig_prod = 0
 while len(dig_prod) < n + 1:
  prodd = i*f
  if digs(prodd) not in list(dig_prod) and all_digs_unique(prodd):
   dig_prod += str(i*f)
   if len(dig_prod) == n:
    if int(dig_prod) > max_prod:
     max_prod = dig_prod
    i += 1
    f = 1
    dig_prod = ''
   elif len(dig_prod) < n:
    f += 1
  else:
   i += 1
   dig_prod = ''
   f = 1
 return max_dig_prod

"""
