
def sharedMotif(fastaList):
    subsPerFasta = findSubstrings(fastaList)
    for x in xrange(0, len(subsPerFasta) - 1):
        commonMotifs = set(subsPerFasta[x]).intersection(subsPerFasta[x + 1])
    longest = max(len(possLongestMotif) for possLongestMotif in commonMotifs)
    return [longestSharedMotif for longestSharedMotif in commonMotifs if len(longestSharedMotif) == longest]

def findSubstrings(fastaList):
    subsPerFasta = []
    for eachFasta in fastaList:
            subsPerFasta.append([eachFasta.getSequence()[i:i+j] for j in range(1,len(eachFasta.getSequence())+1) for i in range(len(eachFasta.getSequence())-j+1)])
    return subsPerFasta









