def in_array(array1, array2):
    # your code
    scores = dict.fromkeys(array1, 0)
    new = array1.copy()
    for idx, a in enumerate(array1):
      for b in array2:
        if a in b:
          scores[a] += 1
      if not scores[a]:
        new.remove(a)
    return sorted(list(set(sorted(new, key=lambda key: scores[key]))))
