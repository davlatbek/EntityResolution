import jellyfish as jf
import codecs

#generate similarity vectors for pair of users for all attributes
def generateSimilarityVectorForUserPair(userpair):
    simvector = []
    userdata1 = userpair[0].split("%")
    userdata2 = userpair[1].split("%")
    for i in xrange(len(userdata1)):
        simvector.append(jf.jaro_winkler(u" ".join(codecs.decode(userdata1[i],"latin-1")),
                                         u" ".join(codecs.decode(userdata2[i],"latin-1"))))
    return simvector

def generateSimilarityVectorsForUserPairs(userpairs):
    vectorlist = list()
    for userpair in userpairs:
        simvector = generateSimilarityVectorForUserPair(userpair)
        vectorlist.append(simvector)
    return vectorlist

#similarity vectors for username only
def generateSimilarityVectorForUsername(userpair):
    simvector = []
    userdata1 = userpair[0].split("%")
    userdata2 = userpair[1].split("%")
    simvector.append(jf.jaro_winkler(u" ".join(codecs.decode(userdata1[0],"latin-1")),
                                     u" ".join(codecs.decode(userdata2[0],"latin-1"))))
    return simvector

def generateSimilarityVectorsForUsernames(userpairs):
    vectorlist = list()
    for userpair in userpairs:
        simvector = generateSimilarityVectorForUsername(userpair)
        vectorlist.append(simvector)
    return vectorlist

def pairResolution(userpairs):
    pairCounter = 0
    for pair in userpairs:
        coeff = generateSimilarityVectorForUsername(pair)
        if coeff[0] > 0.89:
            pairCounter += 1
    return pairCounter/float(len(userpairs))