def score(xorString):
    charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n"
    score = 0
    for i in xorString:
        if i in charSet or i == ' ' or i == '\'':
            score += 1
    return score