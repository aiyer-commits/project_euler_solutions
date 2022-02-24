import unittest


def ld(n, d):
    return n // d, n % d


def digits(num):
    base = 1000
    d = []
    if num < 10:
        return [num]
    while base > 0:
        if num % base == num:
            base //= 10
            continue
        if base == 1:
            d.insert(0, num)
        else:
            d.insert(0, num % base)
        num //= base
        base //= 10

    return d

# assuming no irrational numbers i guess....


def unit_frac(deno):
    slow_numera = 10
    fast_numera = 100
    slow_decifrac = []
    fast_decifrac = []
    cyclic = False
    while not cyclic:
        slow_quo, slow_rem = ld(slow_numera, deno)
        slow_numera = slow_rem*10
        slow_decifrac.extend(digits(slow_quo))

        fast_quo, fast_rem = ld(fast_numera, deno)
        fast_numera = fast_rem*100
        fast_decifrac.extend(digits(fast_quo))
        if fast_decifrac[-1] == slow_decifrac[-1]:
            cyclic = True
        if fast_rem == 0:
            return fast_decifrac
        if slow_rem == 0:
            return slow_decifrac

    return slow_decifrac


def solution(end):
    max_len = 0
    d_max = -1
    for d in range(2, end):
        decifrac = unit_frac(d)
        if len(decifrac) > max_len:
            max_len = len(decifrac)
            d_max = d
            # print(decifrac, d)
        
    return d_max


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(10, 7)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return

    
def decifrac(i):
    return '0.' + ''.join([str(i) for i in unit_frac(i)])

    
if __name__ == "__main__":
    print(solution(999))
    print(unit_frac(982))
    unittest.main()


""" approach
get the decimal fraction part of the number 1/d, using a cycle finding algorithm
count the lengths of the cycles
return the longest length cycle's corresponding d

but how do you do cycle finding in long division?

1/4

slow pointer
1 // 4 = 0 .. place decimal here
multiply 1 by 10..
10 // 4 = 2, 10 % 4 = 2
2 * 10
20 // 4 = 5, 20 % 4 = 0 -> 0.25

fast pointer...

1 // 4 = 0
multiply by 100
100 // 4 = 25, 100 % 4 = 0
stop fast pointer when you hit a 0?
can stop the entire operation...

ok try for 1/7
slow pointer...
1 // 7 = 0, 1 / 7 = 1
10 // 7 = 1, 10 % 7 = 3
30 // 7 = 4, 30 % 7 = 2
20 // 7 = 2, 20 % 7 = 6
60 // 7 = 8, 60 % 7 = 4
40 // 7 = 5, 40 % 7 = 5
50 // 7 = 7, 50 % 7 = 1 <- this is the point where the fast and slow pointer will meet...
10 // 7 = 1, 10 % 7 = 3 ... this is the cycle that we expect

1 // 7 = 0, 1 % 7 = 1
100 // 7 = 14, 100 % 7 = 2
200 // 7 = 28, 200 % 7 = 4
(57,1)
(14,2) ... cycle repeats....


ok how about 1 / 38?
ld(10,38) -> 0,10
ld(100,38) -> 2,24
ld(240,38) -> 6,12
ld(120,38) -> 3,6
ld(60,38) -> 1,22



"""

""" pseudocode

ld(n,d): -> (quotient, remainder)

digits(number): -> [digits]


unit_frac(deno):
 slow_numero = 10
 fast_numero = 100
 slow_decifrac = []
 fast_decifrac = []
 cyclic = False
 while not cyclic:
  slow_quotient, slow_remainder = ld(slow_numero, deno)
  slow_numero = slow_remainder*10
  slow_decifrac.extend(digits(slow_quotient))
  
  fast_quotient, fast_remainder = ld(fast_numero, demo)
  fast_numero = fast_remainder*100
  fast_decifrac.extend(digits(fast_quotient))
  
  if fast_decifrac[-1] == slow_decifrac[-1]: cyclic = True
  if fast_remainder == 0: return fast_decifrac
  if slow_remainder == 0: return slow_decifrac


solution(range_end):
 max_len = 0
 d_max = -1
 for d in range(2,range_end):
  decifrac = unit_frac(d)
  if len(decifrac) > max_len:
   max_len = len(decifrac)
   d_max = d
 return d_max


"""
