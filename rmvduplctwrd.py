temp = []
def remove_duplicate_words(s):
    lst = s.split(" ")
    
    for word in lst:
        if word not in temp:
            temp.append(word)
    
    return " ".join(temp)
    
s='alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
print(remove_duplicate_words(s))