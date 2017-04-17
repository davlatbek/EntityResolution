import random

def findUserLine(user, file):
    datafile = open(file)
    for line in datafile:
        if user.strip("\n\t\r ") in line:
            return line
    return False

def findUserLineBool(user, file):
    datafile = open(file)
    for line in datafile:
        if user in line:
            return True
    return False

def getUserByLineNumber(linenumber, file):
    datafile = open(file)
    lines = datafile.readlines()
    return lines[linenumber]

def checkUsernameInGroundTruth(username1, username2, groundtruth):
    userpair = username1 + " " + username2
    if (findUserLineBool(userpair, groundtruth)):
        print userpair
        return True
    else:
        return False

#check if username pairs are in Ground Truth data and how many of them
def checkNumberOfTruePositivePair(randomuserpairszip, groundtruthdata):
    truePositiveCounter = 0
    trueNegativeCounter = 0
    for pair in randomuserpairszip:
        # getting usernames from random user pairs
        user1 = pair[0].split(" ")[0]
        user2 = pair[1].split(" ")[0]
        if (checkUsernameInGroundTruth(user1, user2, groundtruthdata)):
            truePositiveCounter += 1
        else:
            trueNegativeCounter += 1
    return truePositiveCounter

#generate user pairs that are NOT present in ground truth
def generatePairsNotFromGroundTruth(data1, data2, numberOfPairsToGenerate):
    datafile1 = open(data1)
    datafile2 = open(data2)
    lines1 = datafile1.readlines()
    randnumbers1 = random.sample(xrange(1, len(lines1)), numberOfPairsToGenerate)
    lines2 = datafile2.readlines()
    randnumbers2 = random.sample(xrange(1, len(lines2)), numberOfPairsToGenerate)
    randompairsofnumbers = zip(sorted(randnumbers1), sorted(randnumbers2))

    list1 = list()
    list2 = list()
    i = 1
    while (True):
        for numberpairs in randompairsofnumbers:
            list1.append(getUserByLineNumber(numberpairs[0], data1))
            list2.append(getUserByLineNumber(numberpairs[1], data2))
            i += 1
            if (i > numberOfPairsToGenerate): break
        break
    randomuserpairszip = zip(list1, list2)
    return randomuserpairszip

#generate user pairs that ARE present in ground truth
def generatePairsFromGroundTruth(groundTruthFile, data1, data2, numberOfPairsToGenerate):
    gt = open(groundTruthFile)
    list1 = list()
    list2 = list()
    gtlines = gt.readlines()
    if (numberOfPairsToGenerate>len(gtlines)):
        print "Number of pairs to generate from Ground Truth can't exceed the GT size!"
        return
    i = 1
    while (True):
        for line in gtlines:
            userpair = line.split(" ")
            user1 = findUserLine(userpair[0], data1)
            user2 = findUserLine(userpair[1], data2)
            list1.append(user1)
            list2.append(user2)
            i += 1
            if (i > numberOfPairsToGenerate): break
        break
    userpairzip = zip(list1, list2)
    return userpairzip