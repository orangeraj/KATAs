def getCount(sentence):
 
    vowels = 'aeiou'
    count = 0
    for char in sentence:
        if char in vowels:
            count+=1
    return count

sent = 'ae alone'
print(getCount(sent))


