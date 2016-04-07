
def locateRestrictionSites(fasta):
    allSubs = [(i, fasta.getSequence()[i:i+j]) for j in range(1,len(fasta.getSequence())+1)
               for i in range(len(fasta.getSequence())-j+1)]
    allSubsOfLength = [possRestriction for possRestriction in allSubs if (4 <= len(possRestriction[1]) <= 12)]
    reversePalindromes = [possResPal for possResPal in allSubsOfLength if possResPal[1] == complement(possResPal[1])]
    return reversePalindromes

def complement(sequence):
    protoComplement = ""
    for base in sequence:
        if base == 'A':
            protoComplement = protoComplement + 'T'
        elif base == 'T':
            protoComplement = protoComplement + 'A'
        elif base == 'G':
            protoComplement = protoComplement + 'C'
        elif base == 'C':
            protoComplement = protoComplement + 'G'
    complement = protoComplement[:: -1]
    return complement
