import unittest


def uni_frac(d):
    n = 1
    q = []
    while n != 0 and len(q) < d - 1:
        if n // d == 0:
            n *= 10
            continue
        q.append(n // d)
        if n // d == 0:
            n *= 10
        n = n % d
    return q


def solution(n):
    deno = 2
    longest = 1
    for d in range(2, n+1):
        deci_frac = uni_frac(d)
        len_d = len(deci_frac)
        if len_d > longest:
            longest = len_d
            deno = d
            print(deno, deci_frac)
    return deno


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(10, 7)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    # print(solution(999))
    unittest.main()


""" approach
generate the fractions and count their decimal parts... but the default float representation may not show the entire cycle....

if you treat it like manual long division, you can find cycles using modulo...


ex 1/2 ... 1 // 2 == 0 ... 10 // 2 == 5 ... 10 // 5 == 2 ... terminate? .. 0.5 
 1 // 3 == 0 .... 10 // 3 == 3 ... 10 // 3 == 3 ..... 0.333333 ..
1 // 4 == 0 .... 10 // 4 == 2 .... 10 // 2 == 5 .... 10 // 5 == 2 ... terminate? 0.25
1 // 5 == 0 ... 10 // 5 == 2 ... 10 // 2 == 5 ... terminate 0.2
1 // 6 == 0 ... 10 // 6 == 1 ... 10 // 1 == 10... 10 // 10 == 1 .... terminate ... 0.1101

close... but you have to divide the remainder!!!

1 // 3 == 0, 10 // 3 = 3, 3 // 3 = 1 ...

integer division is wrong, use modulo ?

1 % 3 = 1... ok so don't even deal with the 1 / 3 situation
10 % 3 == 1 ... 1 % 3 = 1 .... 
 hmmmm

10 // 3  == 3,  3 // 3 == 1 ... 1 // 3 == 0, 10 // 3 == 3, 1 // 3 == 0... repeat forever...


do you need both to make a decision of termination?? both integer division and modulo?? 

10 // 3 and 10 % 3 .. integer dvision tells you the divisor and modulo tells you the remainder... 

anything that terminates or has a cycle is a rational number...
anything that does not terminate and does not have a cycle is irrational 

ok.. can safely say that a cycle occurs when? 

"""

""" pseudocode
uni_frac(d):
n = 1
q = []
cyclic = False
while n % d != 0 or not cyclic:
 if n // d == 0:
  n *= 10
  continue
 if n // d in q:
  cyclic = True
 q.append(n // d)
 n = n % d
 
return q


solution(n)
index = 2
longest = 1
for i in range(2,n+1)
 len_i = len(uni_frac(i))
 if len_i > longest:
   longest = len_i
   index = i

return index

"""
