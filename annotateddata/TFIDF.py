from collections import defaultdict
import math
#Term Frequency
def getTF(stemmedCorpus):
    termFrequency = defaultdict(float)
    #print str(stemmedCorpus)
    for v in stemmedCorpus.itervalues():
        if not v is None:
            for word in v:
                termFrequency[word] = termFrequency[word]+1
    maxtf = max(termFrequency.itervalues())
    for k in termFrequency.iterkeys():
        termFrequency[k] = 0.5 + ((termFrequency[k]+0.5)/maxtf)
    return termFrequency

def getIDF(tfdoc1,tfdoc2):
    idf = defaultdict(float)
    for word in tfdoc1.iterkeys():
        if tfdoc2.has_key(word):
            idf[word] = math.log10(2)
        else:
            idf[word] = math.log10(3)

    for word in tfdoc2.iterkeys():
        if not idf.has_key(word):
            idf[word] = math.log10(3)

    return idf
