import re

def increment_string(s):
    m = re.search(r'\d+$', s)
    if m:
      n = m.group()
      return s.replace(n, '') + str(int(n) + 1).zfill(len(n))
    return s + '1'
