def vaporcode(s):
    return " ".join(s.replace(" ","").upper())

s = 'lets go'
print(vaporcode(s))