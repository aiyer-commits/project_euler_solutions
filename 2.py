import unittest


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [(1, 0), (2, 0), (3, 2), (13, 10)]
        for k, summ in cases:
            self.assertEqual(sum_even_fib(k), summ)
        return


"""
generate fibonacci numbers iteratively
if even... add to sum 

summ = 0
fib = [0,1]
while fib[-1] < k:
n1 = fib[-1] + fib[-2]
fib[-2],fib[-1] = fib[-1],n1
if n1 % 2:
summ += n1

return summ



"""


def sum_even_fib(k):
    summ = 0
    fib = [0, 1]
    while fib[-1] < k:
        n1 = fib[-1] + fib[-2]
        if fib[-1] % 2 == 0:
            summ += fib[-1]
        fib[-2], fib[-1] = fib[-1], n1

    return summ


if __name__ == "__main__":
    #unittest.main()
    print(sum_even_fib(4000000))
