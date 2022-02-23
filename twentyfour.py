import unittest


def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def solution(case):
    items_list, lex_index = case
    indices = []
    current_index = 0
    while current_index < lex_index:
        n = item_index = len(items_list)

        if n == 1:
            indices.append(str(items_list.pop()))

            break
        while current_index + item_index * factorial(n - 1) >= lex_index:
            item_index -= 1
        current_index += item_index * factorial(n - 1)
        indices.append(str(items_list.pop(item_index)))

    return "".join(indices)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [
            ((list(range(0, 3)), 1), "012"),
            ((list(range(0, 3)), 6), "210"),
            ((list(range(0, 3)), 3), "102"),
        ]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    print(solution((list(range(0, 10)), 10 ** 6)))
    unittest.main()


""" approach
can this be done without generating all of the lexicographic permutations?
given n items, there are n! permutations...
for a single item, there a n-1! lexicographic permutations...

ok... given a lexicographic index, you can generate the exact permutation without generating all of the preceding ones...


(i-1)*factorial(n-1) ... 


"""

""" pseudocode
factorial(n): ...

solution(items_list, lex_index):
assert(lex_index > 0)
indices = []
current_index = 0
while current_index < lex_index:
 n = item_index = len(items_list)
 if n == 1:
  indices.append(str(items_list.pop()))
  break
 while current_index + item_index*factorial(n-1) > lex_index:
  item_index -= 1
 current_index += item_index * factorial(n-1)
 indices.append(str(items_list.pop(item_index)))

return indices.join('')
"""
