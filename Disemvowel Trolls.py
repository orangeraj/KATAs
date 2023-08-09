def disemvowel(string_):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    string_n = ''
    for char in string_:
        if char not in vowels:
            string_n +=char

    return string_n


print(disemvowel('This website is for losers LOL!'))