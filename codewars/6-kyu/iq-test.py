def iq_test(numbers):
    numbers_even = [int(i) % 2 == 0 for i in numbers.split(' ')]
    numbers_odd = [int(i) % 2 != 0 for i in numbers.split(' ')]
    if sum(numbers_even) > sum(numbers_odd):
      for idx, val in enumerate(numbers_odd):
        if val:
          return idx + 1
    else:
      for idx, val in enumerate(numbers_even):
          if val:
            return idx + 1
