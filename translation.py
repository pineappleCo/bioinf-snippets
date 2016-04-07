import fastaForm

def translate(mRNAFasta):
    translationConv = [('A', ["GCU", "GCC", "GCA", "GCG"]),
                       ('C', ["UGU", "UGC"]),
                       ('D', ["GAU", "GAC"]),
                       ('E', ["GAA", "GAG"]),
                       ('F', ["UUU", "UUC"]),
                       ('G', ["GGU", "GGC", "GGA", "GGG"]),
                       ('H', ["CAU", "CAC"]),
                       ('I', ["AUU", "AUC", "AUA"]),
                       ('K', ["AAA", "AAG"]),
                       ('L', ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"]),
                       ('M', ["AUG"]),
                       ('N', ["AAU", "AAC"]),
                       ('P', ["CCU", "CCC", "CCA", "CCG"]),
                       ('Q', ["CAA", "CAG"]),
                       ('R', ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"]),
                       ('S', ["AGU", "AGC", "UCU", "UCC", "UCA", "UCG"]),
                       ('T', ["ACU", "ACC", "ACA", "ACG"]),
                       ('V', ["GUU", "GUC", "GUA", "GUG"]),
                       ('W', ["UGG"]),
                       ('Y', ["UAU", "UAC"]),
                       ('-', ["UAA", "UAG", "UGA"])]
    codons = [mRNAFasta.getSequence()[i:i+3] for i in range(0, len(mRNAFasta.getSequence()), 3)]
    proteinSeq = ""
    for codon in codons:
        for eachConv in translationConv:
            if codon in eachConv[1]:
                proteinSeq = proteinSeq + eachConv[0]
    protein = fastaForm.ProteinFasta()
    protein.assignAminoSequence(proteinSeq)
    return protein