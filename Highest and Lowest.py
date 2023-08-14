def high_and_low(numbers):
    op = ''
    
    l = numbers.split(' ')
    low = int(l[0])
    high = int(l[0])
    for i in l:

        if int(i) > high:
            high = int(i)
        if int(i) < low:
            low = int(i)

    op = str(high) + " " + str(low)

    return op


s = '-1 -1'
print(high_and_low(s))