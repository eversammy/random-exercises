string = 'zyxwvutsrqponmlkjihgfedcba'
longest = ''
for i in range(len(string)):
    new_string = string[i:]
    substring = new_string[0]
    s_index = 0
    while s_index <= len(new_string) - 2:
        s_index += 1
        if not new_string[s_index] >= substring[-1]:
            break
        else:
            substring += new_string[s_index]
            if len(substring) > len(longest):
                longest = substring
if longest:
    print(longest)
else:
    print(string[0])