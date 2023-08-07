def solution(a, b):
    
    lone = len(a)
    ltwo = len(b)

    if lone > ltwo:
        op = b+a+b
    else:
        op = a+b+a

    return op



a = '111'
b = '22'
print(solution(a,b))