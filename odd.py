
status = True
list = []

def isOdd(num):

    if num % 2 == 0:
        status = False
    else:
        status = True

    for i in range(num+1): #returning numbers
        if i % 2 !=0:
            list.append(i)
        
    print(list)
    return status

print(isOdd(100))