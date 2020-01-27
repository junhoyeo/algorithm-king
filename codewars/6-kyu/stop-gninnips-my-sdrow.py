def spin_words(s):
    return ' '.join([w[::-1] if len(w) > 4 else w for w in s.split(' ')])
