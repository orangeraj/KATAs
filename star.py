'''
for i in range(5,0,-1):
	op = ''
	for j in range(i):
		op += '*'
	print(op)

o/p
*****
****
***
**
*
'''
op = ''
for i in range(5,0,-1):
    if i == 5:
        for j in range(4):
            op += '*'
        print(op)
    else:
        for k in range(4):
            op += ' '
        print(op)
        for l in range(4):
            op += '*'
        print(op)

