
def swap_vowel_case(st):  
    new_st = ''
    char_to_replace = {'a':'A','e':'E','i':'I','o':'O','u':'U','A':'a','E':'e','I':'i','O':'o','U':'u'}
    for char in st:
        if char in char_to_replace:
            new_st += char_to_replace[char]
        else:
            new_st +=char
    return new_st

st = 'C Is AlIvE!'
print(swap_vowel_case(st))