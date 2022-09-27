while True:
    #    Enters a Decimal number
    #    Converts number to Binary
    decimal_number = int(input('Enter Decimal: '))
    number = abs(decimal_number * 2)
    converted = ''
    if number == 0:
        print('0')
    else:
        while number > 1:
            number = number // 2
            w = number % 2
            converted += str(w)
        print('Binary is '+converted[::-1])