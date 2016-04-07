
class NucleicFasta:

    def __init__(self):
        self.id = ""
        self.sequence = ""

    def assignID(self, id):
        self.id = ">" + id

    def assignSequence(self, sequence):
        isSeq = True
        for base in sequence:
            if base != 'A' and base != 'T' and base != 'G' and base != 'C' and base != 'U':
                isSeq = False
        if isSeq:
            self.sequence = sequence
        else:
            print "ERROR: this is not a dna sequence"

    def getID(self):
        return self.id

    def getSequence(self):
        return self.sequence

    def stringify(self):
        print self.id
        print self.sequence

class ProteinFasta:

    def __init__(self):
        self.id = ""
        self.sequence = ""

    def assignID(self, id):
        self.id = ">" + id

    def assignAminoSequence(self, sequence):
        isSeq = True
        aminos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', '*', '-']
        for amino in sequence:
            if amino not in aminos:
                isSeq = False
        if isSeq:
            self.sequence = sequence
        else:
            print "ERROR: this is not a protein"

    def getID(self):
        return self.id

    def getAminoSequence(self):
        return self.sequence

    def stringify(self):
        print self.id
        print self.sequence