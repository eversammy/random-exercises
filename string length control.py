def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.
    """
    count = 1
    new_text = ''
    for item in text.split():
        if count % lineLength == 0:
            new_text += item.replace(item, item + '\n')
        else:
            new_text += item + ' '
        count += 1
    return new_text


s = 'Given text and a desired line length, wrap the text as a typewriter would.'
print(insertNewlines(s, 4))