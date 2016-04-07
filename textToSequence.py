from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def textToBase(text):
    ascii = [ord(char) for char in text]
    sixery = []
    encodedBases = []
    for charCode in ascii:
        sixery.append(sixConverter(charCode))
    for sixCode in sixery:
        encodedBases.append(baseConverter(sixCode))
    return Seq(''.join(encodedBases), IUPAC.unambiguous_dna)

def sixConverter(decimal):
    answer = decimal
    sixCode = []
    while answer != 0:
        sixCode.append(answer % 6)
        answer = answer/6
    return ''.join(map(str, sixCode[::-1]))

def baseConverter(numCode):
    bases = ""
    for char in numCode:
        if char == "0":
            bases = bases + "A"
        elif char == "1":
            bases = bases + "C"
        elif char == "2":
            bases = bases + "G"
        elif char == "3":
            bases = bases + "T"
        elif char == "4":
            bases = bases + "B"
        elif char == "5":
            bases = bases + "P"
    return bases

def pageTag(sequence, spacing):
    seq = str(sequence)
    taggedSeq = "PPP".join([seq[i:i+spacing] for i in range(0, len(seq), spacing)])
    return Seq(taggedSeq, IUPAC.unambiguous_dna)

def pageAddress(sequence):
    tags = sequence.find("PPP")


def quatConverter(decimal):
    answer = decimal
    quatCode = []
    while answer != 0:
        quatCode.append(answer % 4)
        answer = answer/4
    return ''.join(map(str, quatCode[::-1]))









