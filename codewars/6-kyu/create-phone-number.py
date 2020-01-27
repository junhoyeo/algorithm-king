def create_phone_number(n):
    num = ''.join([str(i) for i in n])
    return f'({num[:3]}) {num[3:6]}-{num[-4:]}'
