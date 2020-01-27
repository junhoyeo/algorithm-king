def solution(phone_book):
    for p in phone_book:
        for h in phone_book:
            if len(p) > len(h) and p[:len(h)] == h:
                return False
    return True
