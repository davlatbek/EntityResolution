import ERSerializationAndDegrDistAndRanking as ser

gt = "data/groundtruthflmscleaned"
nodefile1 = "data/flickr.nodes"
edgefile1 = "data/flickr.edges"
nodefile2 = "data/myspace.nodes"
edgefile2 = "data/myspace.edges"

# ser.serializeDict(ser.generateUsernameToIdDict(nodefile1), 'usernametoid1')
# ser.serializeDict(ser.generateUsernameToIdDict(nodefile2), 'usernametoid2')
deserializedusertoid1 = ser.deserializeDict('serialized/usernametoid1.pickle')
deserializedusertoid2 = ser.deserializeDict('serialized/usernametoid2.pickle')

# ser.serializeDict(ser.generateIdToFriendsIdListDict(edgefile1), 'idtofriendlist1')
# ser.serializeDict(ser.generateIdToFriendsIdListDict(edgefile2), 'idtofriendlist2')
idtofriendsidlist1 = ser.deserializeDict('serialized/idtofriendlist1.pickle')
idtofriendsidlist2 = ser.deserializeDict('serialized/idtofriendlist2.pickle')

# ser.serializeDict(ser.generateIdToFirstLevelDegreeDict(nodefile1, idtofriendsidlist1), 'idtofirstleveldegree1')
# ser.serializeDict(ser.generateIdToFirstLevelDegreeDict(nodefile2, idtofriendsidlist2), 'idtofirstleveldegree2')
idtofirstleveldegree1 = ser.deserializeDict('serialized/idtofirstleveldegree1.pickle')
idtofirstleveldegree2 = ser.deserializeDict('serialized/idtofirstleveldegree2.pickle')

# ser.serializeDict(ser.generateIdToSecondLevelDegreeDict(nodefile1, idtofriendsidlist1, idtofirstleveldegree1), 'idtosecondleveldegree1')
# ser.serializeDict(ser.generateIdToSecondLevelDegreeDict(nodefile2, idtofriendsidlist2, idtofirstleveldegree2), 'idtosecondleveldegree2')
idtosecondleveldegree1 = ser.deserializeDict('serialized/idtosecondleveldegree1.pickle')
idtosecondleveldegree2 = ser.deserializeDict('serialized/idtosecondleveldegree2.pickle')

# ser.serializeDict(ser.generateIdPairsFromGroundTruth(gt, deserializedusertoid1, deserializedusertoid2), 'serialized/idpairsfromgt')
pairslist = ser.deserializeDict('serialized/idpairsfromgt.pickle')
# ser.writeIdPairToSecondDegreeToTwoFiles(pairslist, idtosecondleveldegree1, idtosecondleveldegree2, 'results/SLD_GT_firstid.txt', 'results/SLD_GT_secondid.txt')

# ser.serializeDict(ser.generateIdPairsNotFromGroundTruth(nodefile1, nodefile2, 1000), 'serialized/notgtidpairs')
notgtpairslist1 = ser.deserializeDict('serialized/notgtidpairs.pickle')
# ser.writeIdPairToSecondDegreeToTwoFiles(notgtpairslist1, idtosecondleveldegree1, idtosecondleveldegree2, 'results/SLD_NOTGT_firstid.txt', 'results/SLD_NOTGT_secondid.txt')


# Applying Logistic regression to ID TO SECOND LEVEL DEGREE

from sklearn import cross_validation as cv
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsOneClassifier
# target = []
#
# notgtpairs = ser.generateIdPairsNotFromGroundTruth(nodefile1, nodefile2, 200)
# list1 = []
# for id1,id2 in notgtpairs:
#     list1.append([idtosecondleveldegree1[str(id1)],
#                   idtosecondleveldegree2[str(id2)]])
#     target.append(0)
#
# gtpairs = ser.generateIdPairsFromGroundTruth(gt, deserializedusertoid1, deserializedusertoid2)
# for id1,id2 in gtpairs:
#     if id1 in idtosecondleveldegree1:
#         if id2 in idtosecondleveldegree2:
#             list1.append([idtosecondleveldegree1[str(id1)],
#                   idtosecondleveldegree2[str(id2)]])
#             target.append(1)
#
# data = [map(int, x) for x in list1]
#
# d,t = data[:-100], target[:-100]
# res = LogisticRegression()
# res.fit(d,t)
#
# # ovo = OneVsOneClassifier(LogisticRegression()).fit(d,t)
# # print 'Predicted class %s, real class %s' % (ovo.predict(d[-10:]), t[-10:])
# # print 'One vs one accuracy: %.3f' % ovo.score(d,t)
#
#
# print 'Predicted class %s, real class %s' % (res.predict(d[-100:]), t[-100:])
# print 'Probabilities for each class from 0 to 1: %s' % res.predict_proba(d[:])
# print 'One vs one accuracy: %.3f' % res.score(d,t)
#
# i = 0
# j = 0
# one, two = (res.predict(d[-100:]), t[-100:])
# for e1 in one:
#     if  (j >= len(t)):
#         break
#     if (e1 == two.pop(j)):
#         j += 1
#         i += 1
# print i/100.0



# ser.serializeDict(ser.sortrankbysecondleveldegree(idtosecondleveldegree1), 'serialized/idtorank1')
idtorank1 = ser.deserializeDict('serialized/idtorank1.pickle')
# ser.serializeDict(ser.sortrankbysecondleveldegree(idtosecondleveldegree2), 'serialized/idtorank2')
idtorank2 = ser.deserializeDict('serialized/idtorank2.pickle')







# WRITE ID TO RANKING RESULTS TO FILE
# file11 = 'results/idtorank11.txt'
# file12 = 'results/idtorank11.txt'
# f11 = open(file11, 'w')
# f12 = open(file12, 'w')
# for id1 in idtorank1:
#     f11.write(idtorank1[id1])
#     f12.write()





# Applying Logistic Regression to RANKING TO SECOND LEVEL DEGREE
target = []

notgtpairs = ser.generateIdPairsNotFromGroundTruth(nodefile1, nodefile2, 500)
list1 = []
for id1,id2 in notgtpairs:
    list1.append([idtorank1[id1],
                  idtorank2[id2]])
    target.append(0)

gtpairs = ser.generateIdPairsFromGroundTruth(gt, deserializedusertoid1, deserializedusertoid2)
for id1,id2 in gtpairs:
    if int(id1) not in idtorank1:
        continue
    if int(id2) not in idtorank2:
        continue
    list1.append([idtorank1[int(id1)], idtorank2[int(id2)]])
    target.append(1)

print "taget %s", target

data = [map(int, x) for x in list1]
d,t = data[0::2], target[0::2]
d1,t1 = data[1::2], target[1::2]
res = LogisticRegression()
res.fit(d,t)

# ovo = OneVsOneClassifier(LogisticRegression()).fit(d,t)
# print 'OVOPredicted class %s, real class %s' % (ovo.predict(d[-100:]), t[-100:])
# print 'OVO One vs one accuracy: %.3f' % ovo.score(d,t)

print 'Predicted class %s, real class %s' % (res.predict(d1[1::2]), t1[1::2])
print 'Probabilities for each class from 0 to 1: %s' % res.predict_proba(d1[1::2])
print 'Accuracy: %.3f' % res.score(d1,t1)

#calculate accuracy
i = 0
one, two = res.predict(d[-100:]), t[-100:]
print "Calculated accuracy %s", i/100.0








