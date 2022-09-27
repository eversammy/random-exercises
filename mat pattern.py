"""
Random mat  pattern
"""
mat_w = input("Enter 'w' for mat-width or 'any other string' for mat-height: ")
mat_value = input('Enter Value: ')
mat = int(mat_value) if mat_w == 'w' else int(mat_value) * 3
mat_upper, mat_lower = [i for i in range(3, (mat//3)+1, 2)], [i for i in reversed(range(3, (mat//3)+1, 2))]
welcome = '-' * ((mat-7)//2) + 'WELCOME' + '-' * ((mat-7)//2)
for u in mat_upper:
    sheet = '-' * (int((mat - ((u / 2) - 1) * 6) / 2)) + '.' + ((u // 2) - 1) * ('|' + '.' + '.') + '|' + (
            (u // 2) - 1) * ('.' + '.' + '|') + '.' + '-' * (int((mat - ((u / 2) - 1) * 6) / 2))
    print(sheet)
print(welcome)
for u in mat_lower:
    sheet = '-' * (int((mat - ((u / 2) - 1) * 6) / 2)) + '.' + ((u // 2) - 1) * ('|' + '.' + '.') + '|' + (
            (u // 2) - 1) * ('.' + '.' + '|') + '.' + '-' * (int((mat - ((u / 2) - 1) * 6) / 2))
    print(sheet)
