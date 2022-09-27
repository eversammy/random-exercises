first_num = int(input('Enter first number: '))
#   Takes two(2) integers
#   Returns all prime numbers between the integers in a list
second_num = int(input('Enter second number: '))
z = (first_num, second_num)
prime_num = []
for item in range(first_num, second_num):
    if item > 1:
        for digit in range(2, item):
            if item % digit == 0:
                break
        else:
            prime_num.append(item)
print(f'''Prime numbers between {first_num} and {second_num}:
{prime_num}''')
