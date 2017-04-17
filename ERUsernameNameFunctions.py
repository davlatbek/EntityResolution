import codecs

# gets pair of users to the input and outputs the coefficient of similarity
# weights:
# username  location    gender  e-mail  name
# 0.8909    0.7468      0.2786  0.98    0.85

class Thresholds:
    username = 0.89
    name = 0.75
    gender = 0.27
    location = 0.75

class Weights:
    username = .7
    name = .3

#generalized version for username where you can delegate different functions for string comparison
def genSimVecUsername(userpair, comparisonFunction):
    compare = comparisonFunction
    simvector = []
    userdata1 = userpair[0].split("%")
    userdata2 = userpair[1].split("%")
    simvector.append(compare(u" ".join(codecs.decode(userdata1[0],"latin-1")),
                                     u" ".join(codecs.decode(userdata2[0],"latin-1"))))
    return simvector

def pairResolutionWithFunction(userpairs, comparisonFunction):
    pairCounter = 0
    for pair in userpairs:
        coeff = genSimVecUsername(pair, comparisonFunction)
        if coeff[0] > 0.89:
            pairCounter += 1
    return pairCounter/float(len(userpairs)), pairCounter

def genSimVecForTwoAttr(userpair, comparisonFunction):
    compare = comparisonFunction
    simvector = []
    userdata1 = userpair[0].split("%")
    userdata2 = userpair[1].split("%")
    simvector.append(compare(u" ".join(codecs.decode(userdata1[0],"latin-1")),
                                     u" ".join(codecs.decode(userdata2[0],"latin-1"))))
    simvector.append(compare(u" ".join(codecs.decode(userdata1[1], "latin-1")),
                             u" ".join(codecs.decode(userdata2[1], "latin-1"))))
    return simvector


def pairResolutionWithFuncForTwoAttr(userpairs, comparisonFunction):
    pairCounter = 0
    for pair in userpairs:
        coeff = genSimVecForTwoAttr(pair, comparisonFunction)
        if (coeff[0] is None or coeff[1] is None):
            continue
        resultingcoef = coeff[0]*.8 + coeff[1]*.2
        if resultingcoef > .77:
            pairCounter += 1
    # return pairCounter/float(len(userpairs)), pairCounter
    return pairCounter


def computeScore(userpairsGT, userpairsNotGT, comparisonFunction):
    truepositive = pairResolutionWithFuncForTwoAttr(userpairsGT, comparisonFunction)
    falsenegative = pairResolutionWithFuncForTwoAttr(userpairsNotGT, comparisonFunction)

    falsepositive = float(len(userpairsGT)) - float(truepositive)
    precision = float(truepositive)/(float(truepositive) + falsepositive)

    truenegative = float(len(userpairsNotGT)) - float(falsenegative)
    recall = float(truepositive)/(float(truepositive) + falsenegative)

    f1score = 2.0*(precision*recall)/(precision+recall)
    accuracy = (float(truepositive) + float(truenegative))/(truepositive + truenegative + falsepositive + falsenegative)
    return round(precision,2), round(recall,2), round(f1score,2)



