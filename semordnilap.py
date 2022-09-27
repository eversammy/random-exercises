def semordnilap(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return True
    elif len(str1) != len(str2):
        return False
    elif str1[0] != str2[-1]:
        return False
    else:
        return semordnilap(str1[1:], str2[:-1])

w = semordnilap('rits live oo', 'o evil stir')
print(w)