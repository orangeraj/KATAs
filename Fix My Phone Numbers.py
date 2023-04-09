def is_it_a_num(s: str) -> str:
    validate_against = '0123456789'
    out = ''
    for char in s:
        if char in validate_against:
           out+=char
        else:
            pass
    if out.startswith('0'):
        if len(out) == 11:
            return out
        else:
            return 'Not a phone number'
    else:
        return 'Not a phone number'

    

s = 'efRFS:)0207ERGQREG88349F82!'
print(is_it_a_num(s))