
swaped = ''
def swap(word):
    global swaped

    for i in word:
        
        if i.islower():
            swaped+= i.upper()
        else:
            swaped+=i.lower()

    return swaped
print(swap('RaJaS mhatrT'))