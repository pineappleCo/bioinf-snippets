from itertools import product

def enumLex(alphabet, length):
    return [''.join(x) for x in product(alphabet, repeat=length)]
