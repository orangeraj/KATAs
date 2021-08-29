
temp = []
string_n = ''
new_string = ''
def remove_duplicate(words):
    global temp
    global string_n
    global new_string

    lst = words.split(' ')

    for i in lst:
        if i not in temp:
            temp.append(i)

    new_string = ' '.join(temp)
    return new_string

words = ("my cat is my cat fat")
print(remove_duplicate(words))

