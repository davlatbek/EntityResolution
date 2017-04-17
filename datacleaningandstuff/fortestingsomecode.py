import ERSerializationAndDegrDistAndRanking as ser

idtofirstleveldegree1 = ser.deserializeDict('../serialized/idtofirstleveldegree1.pickle')
idtofirstleveldegree2 = ser.deserializeDict('../serialized/idtofirstleveldegree2.pickle')

i = 0
for k, v in idtofirstleveldegree1.items():
    if (i > 100):
        break
    print k, v
    i += 1


i = 0
for k, v in idtofirstleveldegree2.items():
    if (i > 10):
        break
    print k, v
    i += 1