
string =''
lower_list = []

def lowercase(lst):
    global string
    global lower_string

    for i in lst: #converting list to string
        string += i + 'x'

    lower_string = string.lower()
    lower_string[:-1] #removing last character from string
    lower_list = lower_string.split('x')

    return lower_list[:-1] #removing last item from list

lst = ['rajas','harshIt','ApPlE']
print(lowercase(lst))

'''
list = ['RajAs', ' hjarsHIT']
list2 = []
for i in list:
    list2.append(i.lower())

print(list2)'''