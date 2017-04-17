import ERGenerateUserpairs as gu
import ERUsernameNameFunctions as er
import similarityfunctions as sf
import jellyfish as jf

datafile1 = "data/flickrdata.txt"
datafile2 = "data/myspacedata.txt"
groundtruthdata = "data/groundtruthflmscleaned"

userPairsGT = gu.generatePairsFromGroundTruth(groundtruthdata, datafile1, datafile2, 443)
userPairsNotGT = gu.generatePairsNotFromGroundTruth(datafile1, datafile2, 2000)

# for username only
# print cu.pairResolutionWithFunction(userPairsGT, jf.match_rating_comparison)
# print cu.pairResolutionWithFunction(userPairsGT, jf.jaro_winkler)
# print cu.pairResolutionWithFunction(userPairsGT, jf.jaro_distance)
# print cu.pairResolutionWithFunction(userPairsGT, sf.jaccard_similarity)
# print cu.pairResolutionWithFunction(userPairsNotGT, sf.jaccard_similarity)
# print cu.pairResolutionWithFunction(userPairsNotGT, jf.jaro_distance)
# print cu.pairResolutionWithFunction(userPairsNotGT, jf.jaro_winkler)
# print cu.pairResolutionWithFunction(userPairsNotGT, jf.match_rating_comparison)

# for username+name attributes
print er.pairResolutionWithFuncForTwoAttr(userPairsGT, jf.jaro_winkler)
print er.pairResolutionWithFuncForTwoAttr(userPairsGT, jf.jaro_distance)
print er.pairResolutionWithFuncForTwoAttr(userPairsGT, sf.jaccard_similarity)
print er.pairResolutionWithFuncForTwoAttr(userPairsNotGT, sf.jaccard_similarity)
print er.pairResolutionWithFuncForTwoAttr(userPairsNotGT, jf.jaro_distance)
print er.pairResolutionWithFuncForTwoAttr(userPairsNotGT, jf.jaro_winkler)

# f1 and accuracy
print er.computeScore(userPairsGT, userPairsNotGT, jf.jaro_winkler)
print er.computeScore(userPairsGT, userPairsNotGT, jf.jaro_distance)
print er.computeScore(userPairsGT, userPairsNotGT, sf.jaccard_similarity)
