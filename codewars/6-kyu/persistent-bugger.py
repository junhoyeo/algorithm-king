from functools import reduce
import operator

def prod(factors):
    return reduce(operator.mul, factors, 1)

def persistence(n):
    count = 0
    while len(str(n)) > 1:
      n = prod([int(i) for i in str(n)])
      count += 1
    return count
