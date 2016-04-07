import nucleotideCounter

def cgContent(sequence):
    total = sum(nucleotideCounter.nucCount(sequence, "ATCG"))
    cg = sum(nucleotideCounter.nucCount(sequence, "CG"))
    cgContent = (cg/float(total)) * 100
    return cgContent

