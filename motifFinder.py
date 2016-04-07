import itertools

def findMotif(toSearch, motif):
    seq = toSearch.getSequence()
    i = 0
    occurrences = ()
    while i < len(seq):
        i = seq.find(motif, i)
        if i == -1:
            break
        occurrences.append(i)
        i = i + len(motif)
    return occurrences

def findSplicedMotif(toSearch, subsequence):
    searchSeq = toSearch.getSequence()
    seq = subsequence.getSequence()
    positions = []
    for eachBase in seq:
        positions.append([i[0] for i in enumerate(searchSeq) if i[1] == eachBase])
    permutations = list(itertools.product(*positions))
    orderedPerms = [perm for perm in permutations if perm == tuple(sorted(perm))]
    return orderedPerms







