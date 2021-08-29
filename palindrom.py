string = 'rajas'

#python
'''
string_r = string[::-1]
if string == string_r:
    print('palindrom')
else:
    print('not palindrom')
'''
#if reverse function not available
list = []
count = 0
for letter in string:
    list.append(letter)

for i in range(len(list)-1):
    if list[i] == list[(len(list)-1)-i]:
        count += 0
    else:
        count += 1
if count==0:
    print('palindrom')
else:
    print('not palindrom')
