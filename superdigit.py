
number = 148
round = 3
st_c = ''
result = 0
for count in range(round):
    st_c+=str(number) #148148148

num = int(st_c)
print(num)
#print(st_c)

while len(str(num)) > 1:
    #for i in range(len(st_c)):

    for item in str(num):
        result += int(item) #39
        print(num)
num = result  

    #num = total
    #digit = num % 10
    #result = result + digit
    #num = num//10
print(num)





