def order(sentence):
  if not sentence:
    return ''
  words = sentence.split(' ')
  return ' '.join(sorted(words, key=lambda w: [int(i) for i in w if i.isdigit()][0]))
