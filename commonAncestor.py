
def commonAncestor(sequenceList):
    # assumes all entries in sequenceList are same length
    # if multiple possible consensus sequences then only returns one
    # when picking which of multiple consensus sequences bias is given in the follow order A, C, G, T
    aS = []
    cS = []
    gS = []
    tS = []
    for x in xrange(0, len(str(sequenceList[0]))):
        aS.append(0)
        cS.append(0)
        gS.append(0)
        tS.append(0)
    for eachSequence in sequenceList:
        x = 0
        for eachBase in str(eachSequence):
            if eachBase == 'A':
                aS[x] = aS[x] + 1
            elif eachBase == 'C':
                cS[x] = cS[x] + 1
            elif eachBase == 'G':
                gS[x] = gS[x] + 1
            elif eachBase == 'T':
                tS[x] = tS[x] + 1
            x = x + 1
    consensus = ""
    for x in xrange(0, len(str(sequenceList[0]))):
        if aS[x] == max(aS[x], cS[x], gS[x], tS[x]):
            consensus = consensus + 'A'
        elif cS[x] == max(aS[x], cS[x], gS[x], tS[x]):
            consensus = consensus + 'C'
        elif gS[x] == max(aS[x], cS[x], gS[x], tS[x]):
            consensus = consensus + 'G'
        elif tS[x] == max(aS[x], cS[x], gS[x], tS[x]):
            consensus = consensus + 'T'
    return consensus





















