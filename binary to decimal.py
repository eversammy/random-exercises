while True:
    #    Enters a Binary number in decimal
    #    Converts number to Decimal
    binary_number = abs(int(input('Enter Binary: ')))
    aa = any(i in list(str(binary_number)) for i in list('23456789'))
    if aa is False:
        number = str(binary_number)
        length = len(number)
        x = 0
        y = 0
        converted = 0
        while x < length:
            x += 1
            formula = int(number[-x]) * (2 ** y)
            converted += formula
            y += 1
        print('Decimal is ' + str(converted))
    else:
        print('Invalid Binary Number')
