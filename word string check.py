def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.
    """
    f = []
    tot = 0
    for i in range(len(x)):
        f.append(word.index(x[i]))
        if len(f) > 2:

            if f[-1] > f[-2]:
                tot += 1
    print(len(f), tot)

    if len(f) - 2 == tot:
        return True
    else:
        return False


d =x_ian('eric', 'meritocracy')
print(d)

