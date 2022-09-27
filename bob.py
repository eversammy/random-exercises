s = 'azcbobobegghakl'
count = 0
x, y = -1, 2
while y <= len(s)-1:
    x += 1
    y += 1
    if s[x:y] == 'bob':
        count += 1
print('Number of times bob occurs is:', s[x:y], count)