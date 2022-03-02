import unittest


def unique_digs(n):
    digits = digs(n)
    if len(set(digits)) == len(digits):
        return True
    return False


def digs(n):
    base = 1000
    digits = []
    while base > 0:
        if n % base == n:
            base //= 10
            continue
        digits.append(n // base)
        n = n % base
        base //= 10
    return digits
        

def solution():
    return_value = 0
    digits = list(range(1, 10))
    tested_prods = set()
    for i_fdp, fdp in enumerate(digits):
        ps_digits = [d for d in digits if d != fdp]
        for i_sdp, sdp in enumerate(ps_digits):
            pt_digits = [d for d in ps_digits if d != sdp]
            for i_tdp, tdp in enumerate(pt_digits):
                pfo_digits = [d for d in pt_digits if d != tdp]
                for fodp in pfo_digits:
                    prod_digs = [fdp, sdp, tdp, fodp]
                    product = 1000*fdp + 100*sdp + 10*tdp + fodp
                    rem_digs = [d for d in digits if d not in prod_digs]
                    for single_dig_mult in rem_digs:
                        if single_dig_mult == 1:
                            continue
                        if product % single_dig_mult == 0:
                            
                            multiplier = product // single_dig_mult
                            multiplier_digs = digs(multiplier)
                            
                            overlap_digs = [d for d in multiplier_digs if d in prod_digs or d == single_dig_mult]
                            all_digs = set().union(*[prod_digs, multiplier_digs])
                            all_digs.add(single_dig_mult)
                        
                            if len(overlap_digs) == 0 and unique_digs(multiplier) and product not in tested_prods and all_digs == set(digits):
                                tested_prods.add(product)
                                return_value += product
                    for i_fdm, fdm in enumerate(rem_digs):
                        psdm_digits = [d for d in rem_digs if d != fdm]
                        for sdm in psdm_digits:
                            multi_digs = [fdm, sdm]
                            multiplicand = 10 * fdm + sdm
                            if product % multiplicand == 0:
                                multiplier = product // multiplicand
                                multiplier_digs = digs(multiplier)
                                overlap_digs = [d for d in multiplier_digs if d in prod_digs or d in multi_digs]
                                all_digs = set().union(*[prod_digs, multi_digs, multiplier_digs])
                                if len(overlap_digs) == 0 and unique_digs(multiplier) and product not in tested_prods and all_digs == set(digits):
                                    tested_prods.add(product)
                                    return_value += product
                                
    return return_value


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
a * b = c ... each digit 1 to n must be represented at least and at most once.
< 123456789
4 < digs(c) < n - 2 ... n > 4 in the first place... 
2 < digs(a) + digs(b) < 5

for digs 1-9
4 < digs(a) + digs(b) <= 5
4 <= digs(c)

division approach:
pick a 4 digit number made of 4 unique digits
generate factors using the remaining five digits, from least to greatest... 
find divisor pairs... check if they satisfy the remaining 5 digits... 



"""

""" pseudocode
sol(n)
return_value = 0
digits = list range 1,n+1
for i_fd, first_digit in enum(digits):
 for second_digit in digits[i_fd+1 % len(digits):i_fd]:
  for third_digit in digits[i_sd+1 % len(digits):i_fd]:
   for fourth_digit in digits[i_td+1 % len(digits):i_fd]:
     number = 1000*first_digit + 100 * second_digit + 10 * third_digit + fourth_digit
     remaining_digits = [d for d in digits if d not in [first,second,third,fourth]]
     for i_fdm, fdm in enum rem:
       for i_sd, sdm in enum rem[i_fdm+1 % len rem]:
          multiplicand = 10*fdm + sdm
          if number % multiplicand == 0:
           multiplier = number / multiplicand
           overlapping_digs = [d for d in digs(multiplier) if d in product_digs or d in remaining_digs]
           if len(overlapping_digs) == 0:
              return_value += number 

return return_value
"""
