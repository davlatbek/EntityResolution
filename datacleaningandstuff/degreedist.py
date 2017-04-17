
#===================================================
                    # DEPRECATED
#===================================================


# def findFirstLevelUserIds(username, nodefile):
#     userids = []
#     pass
#
# def findSecondLevelUserIds(username):
#     userids = []
#     pass
#
# def overlappingNumberOfSecondLevelUserIds(username1, usernmae2):
#     pass

def findUserIdByUsername(username, file):
    datafile = open(file)
    for line in datafile:
        if username.strip("\n\t\r ") in line:
            res = line.split("\t")
            datafile.close()
            return res[0]
    datafile.close()
    return False

def findUserIdDegree(userid, edgefile):
    filenode = open(edgefile)
    counter = 0
    for line in filenode:
        res = line.split(" ")
        if (res[0].strip("\r\t\n ") == userid or res[1].strip("\r\t\n ") == userid):
            counter += 1
            continue
        else:
            continue
    filenode.close()
    return counter

def findFriendIdsOfUserId(userid, file):
    filenode = open(file)
    friendids = []
    for line in filenode:
        res = line.split(" ")
        if (res[0].strip("\r\t\n ") == userid or res[1].strip("\r\t\n ") == userid):
            if (res[0].strip("\r\t\n ") == userid):
                friendids.append(res[1].strip("\r\t\n "))
            else:
                friendids.append(res[0].strip("\r\t\n "))
    filenode.close()
    return friendids

#first level degree distribution, returns list of degrees for friends of username
def findSecondLevelDegree(username, edgefile):
    degree = []
    for id in findFriendIdsOfUserId(username, edgefile):
        degree.append(findUserIdDegree(id, edgefile))
    return degree