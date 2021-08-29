
lst_lowered = []
s1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def lower(lst):
    global lst_lowered

    for i in lst:
        for j in range(len(s1)-1):
            if i == s1[j]:
                index1 = s1.index(s1[j])
                lst_lowered.append(s2[index1])
            elif i == s2[j]:
                index2 = s2.index(s2[j])
                lst_lowered.append(s1[index2])


    return lst_lowered



l = ['Y','f','T']
print(lower(l))