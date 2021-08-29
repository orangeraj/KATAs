
#getting substrings from input string

def Subs(s):
    max_l = 0
    for i in range(len(s)):
        for j in range (i,len(s)+1):
            sub_s = s[i:j]
            
            #checking if substring is palidrom or not
            sub_sr = sub_s[::-1]

            if sub_sr == sub_s:
                if len(sub_sr) > max_l:
                    max_l = len(sub_sr) 
                    print(sub_sr)   
                else:
                    pass
            else:
                pass
                
    return  max_l

s ='rarajasajarr'
print(Subs(s))
