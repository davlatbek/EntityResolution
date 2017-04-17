# clean ground truth file from error lines
gt = open("../data/groundtruthflmscleaned", "r+")
d = gt.readlines()
gt.seek(0)

for i in d:
    if "error" not in i:
        gt.write(i)

gt.truncate()
gt.close()

# #clean userdata files from error users
# gt = open("myspacedata.txt", "r+")
# d = gt.readlines()
# gt.seek(0)
#
# for i in d:
#     if "error" not in i:
#         gt.write(i)
#
# gt.truncate()
# gt.close()