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
ser.writeIdPairToSecondDegreeToTwoFiles(pairslist, idtosecondleveldegree1, idtosecondleveldegree2, 'results/SLD_GT_firstid.txt', 'results/SLD_GT_secondid.txt')

# ser.serializeDict(ser.generateIdPairsNotFromGroundTruth(nodefile1, nodefile2, 1000), 'serialized/notgtidpairs')
notgtpairslist1 = ser.deserializeDict('serialized/notgtidpairs.pickle')
ser.writeIdPairToSecondDegreeToTwoFiles(notgtpairslist1, idtosecondleveldegree1, idtosecondleveldegree2, 'results/SLD_NOTGT_firstid.txt', 'results/SLD_NOTGT_secondid.txt')




#====================================================
# Applying Logistic regression TO FIRST LEVEL DEGREE
from sklearn.linear_model import LogisticRegression

ser.serializeDict(ser.sortrankbysecondleveldegree(idtosecondleveldegree1), 'serialized/idtorankbyfirstlevel1')
idtorankbyfld1 = ser.deserializeDict('serialized/idtorankbyfirstlevel1.pickle')
ser.serializeDict(ser.sortrankbysecondleveldegree(idtosecondleveldegree2), 'serialized/idtorankbyfirstlevel2')
idtorankbyfld2 = ser.deserializeDict('serialized/idtorankbyfirstlevel2.pickle')

# Applying Logistic Regression to RANKING TO FIRST LEVEL DEGREE
target = []
notgtpairs = ser.generateIdPairsNotFromGroundTruth(nodefile1, nodefile2, 1000)
list1 = []
for id1,id2 in notgtpairs:
    list1.append([idtorankbyfld1[id1],
                  idtorankbyfld2[id2]])
    target.append(0)

gtpairs = ser.generateIdPairsFromGroundTruth(gt, deserializedusertoid1, deserializedusertoid2)
for id1,id2 in gtpairs:
    if int(id1) not in idtorankbyfld1:
        continue
    if int(id2) not in idtorankbyfld2:
        continue
    list1.append([idtorankbyfld1[int(id1)], idtorankbyfld2[int(id2)]])
    target.append(1)

data = [map(int, x) for x in list1]
d,t = data[0::2], target[0::2]
d1,t1 = data[1::2], target[1::2]
res = LogisticRegression()
res.fit(d,t)

print 'Predicted class %s, real class %s' % (res.predict(d1), t1)
print 'Probabilities for each class from 0 to 1: %s' % res.predict_proba(d1[1::2])
print 'Accuracy: %.3f' % res.score(d1,t1)