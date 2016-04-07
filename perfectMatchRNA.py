import math

def matchCount(rnaFasta):
    seq = rnaFasta.getSequence()
    count = seq.count('A')
    a = math.factorial(count)
    c = math.factorial((len(seq) - (2 * count))/2)
    return a * c
