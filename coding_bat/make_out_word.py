


def make_out_word(out, word):
    zmienna = out[((len(out))/2):] + word + out[:((len(out))/2)]
    return zmienna


print(make_out_word("<<>>","word"))

len(out)