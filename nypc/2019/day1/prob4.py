import re

def valid(email):
    try:
        local, domain = email.split('@')
        reg = re.compile('^[a-zA-Z0-9-\\.]+$')
        if reg.match(local) and reg.match(domain):
            return True
        return False
    except:
        return False

print(*[
    'Yes' if valid(input()) else 'No'
    for _ in range(int(input()))
], sep='\n')
