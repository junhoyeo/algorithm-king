def find_it(seq):
    n = {}
    for s in seq:
      if s in n:
        n[s] += 1
      else: 
        n[s] = 0
    for i in n.keys():
      if n[i] % 2 == 0:
        return i
    return None
