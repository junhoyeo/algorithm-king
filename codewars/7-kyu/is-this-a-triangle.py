def is_triangle(a, b, c):
    if any(i > 0 for i in [a, b, c]):
      return a + b > c and b + c > a and a + c > b
    return False
