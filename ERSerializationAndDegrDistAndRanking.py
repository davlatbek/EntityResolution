import cPickle as pickle
import random as rand

def serializeDict(dictionary, tofilename):
    with open(tofilename + '.pickle', 'wb') as handle:
        pickle.dump(dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)

def deserializeDict(fromfile):
    with open(fromfile, 'rb') as handle:
        return pickle.load(handle)

def generateUsernameToIdDict(nodefile):
    nodefile = open(nodefile)
    idtousernamedict = {}
    for line in nodefile.xreadlines():
        res = line.split("\t")
        idtousernamedict[res[1].strip("\t\r\n ")] = res[0].strip("\t\r\n ")
    nodefile.close()
    return idtousernamedict

def generateIdToFriendsIdListDict(edgefile):
    idtofriendlistdict = {}
    edgefile = open(edgefile)
    for line in edgefile:
        res = line.split(" ")
        id1 = res[0].strip("\r\t\n ")
        id2 = res[1].strip("\r\t\n ")
        if (id1 in idtofriendlistdict):
            idtofriendlistdict[id1].append(id2)
        else:
            idtofriendlistdict[id1] = [id2]

        if (id2 in idtofriendlistdict):
            idtofriendlistdict[id2].append(id1)
        else:
            idtofriendlistdict[id2] = [id1]
    edgefile.close()
    return idtofriendlistdict

def generateIdToFirstLevelDegreeDict(nodefile, idtofriendsidlistdict):
    idtofirstleveldegreedict = {}
    nodefile = open(nodefile)
    for line in nodefile:
        res = line.split("\t")
        id = res[0].strip("\t\r\n ")
        if (id not in idtofirstleveldegreedict):
            idtofirstleveldegreedict[id] = len(idtofriendsidlistdict[id])
        else:
            idtofirstleveldegreedict[id] = len(idtofriendsidlistdict[id])
    nodefile.close()
    return idtofirstleveldegreedict

def generateIdToSecondLevelDegreeDict(nodefile, idtofriendsidlistdict, idtofirstleveldegreedict):
    idtosecondleveldegreedict = {}
    nodefile = open(nodefile)
    for line in nodefile.xreadlines():
        res = line.split("\t")
        id = res[0].strip("\r\t\n ")
        numberofsecondlevelfriends = 0
        for friendid in idtofriendsidlistdict[id]:
            numberofsecondlevelfriends += idtofirstleveldegreedict[friendid]
        if (id not in idtosecondleveldegreedict):
            idtosecondleveldegreedict[id] = numberofsecondlevelfriends
    nodefile.close()
    return idtosecondleveldegreedict

def generateIdPairsFromGroundTruth(groundtruthfile, usernametoiddict1, usernametoiddict2):
    tuples = ()
    pairslist = list(tuples)
    groundfile = open(groundtruthfile)
    for line in groundfile.readlines():
        res = line.split(" ")
        username1 = res[0].strip("\r\t\n ")
        username2 = res[1].strip("\r\t\n ")
        if (username1 in usernametoiddict1 and username2 in usernametoiddict2):
            id1 = usernametoiddict1[username1]
            id2 = usernametoiddict2[username2]
            pairslist.append((id1, id2))
    groundfile.close()
    return pairslist

def generateIdPairsNotFromGroundTruth(nodefile1, nodefile2, numberOfPairsToGenerate):
    tuples = ()
    notgtpairslist = list(tuples)
    file1 = open(nodefile1)
    file2 = open(nodefile2)
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    randnumbers1 = rand.sample(xrange(1, len(lines1)), numberOfPairsToGenerate)
    randnumbers2 = rand.sample(xrange(1, len(lines2)), numberOfPairsToGenerate)
    randompairsofnumbers = zip(randnumbers1, randnumbers2)
    i = 1
    while (True):
        for numberpairs in randompairsofnumbers:
            notgtpairslist.append((numberpairs[0], numberpairs[1]))
            i += 1
            if (i > numberOfPairsToGenerate):
                break
        break
    file1.close()
    file2.close()
    return notgtpairslist

def writeIdPairToSecondDegreeToFile(useridpairs, usernametoiddict1, usernametoiddict2, idtosecondleveldegreedict1, idtosecondleveldegreedict2, tofile):
    file = open(tofile, 'w')
    for useridpair in useridpairs:
        id1 = useridpair[0]
        id2 = useridpair[1]
        if (id1 in idtosecondleveldegreedict1) and (id2 in idtosecondleveldegreedict2):
            file.write(str(idtosecondleveldegreedict1[id1]) + ' ' + str(idtosecondleveldegreedict2[id2]) + '\n')
    file.close()

def writeIdPairToSecondDegreeToTwoFiles(useridpairs, idtosecondleveldegreedict1, idtosecondleveldegreedict2, tofile1, tofile2):
    file1 = open(tofile1, 'w')
    file2 = open(tofile2, 'w')
    for useridpair in useridpairs:
        id1 = useridpair[0]
        id2 = useridpair[1]
        # if (id1 in idtosecondleveldegreedict1 and id2 in idtosecondleveldegreedict2):
        one = str(idtosecondleveldegreedict1[str(id1)])
        two = str(idtosecondleveldegreedict2[str(id2)])
        file1.write(one + '\n')
        file2.write(two + '\n')
    file1.close()
    file2.close()

# sort by number of first level degree in two networks
# return list of tuples (id, rank (by first level))
def sortrankbyfirstleveldegree(idtofirstleveldegree):
    rankinglist = []
    idtorankdict = {}
    for k, v in idtofirstleveldegree.iteritems():
        rankinglist.append([k,v])
    rankingsortedbyvalue = sorted(rankinglist, key=lambda tup: tup[1], reverse=True)

    i = 1
    for k, v in rankingsortedbyvalue:
        idtorankdict[int(k)] = i
        i += 1
    return idtorankdict

# sort by number of second level degree in two networks
# return list of tuples (id, rank (second level degree))
def sortrankbysecondleveldegree(idtosecondleveldegreedict):
    rankinglist = []
    idtorankdict = {}
    for k, v in idtosecondleveldegreedict.iteritems():
        rankinglist.append([k,v])
    rankingsortedbyvalue = sorted(rankinglist, key=lambda tup: tup[1], reverse=True)

    i = 1
    for k, v in rankingsortedbyvalue:
        idtorankdict[int(k)] = i
        i += 1
    return idtorankdict
