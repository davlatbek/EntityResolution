import jellyfish as jf

#Levenstein
def lenenstein_distance(str1, str2):
    pass

#Q-grams
def qgrams(str1, str2):
    pass

#jaccard_similarity algorithm
def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)

def jaro_winkler(str1, str2):
    return jf.jaro_winkler(unicode(str1), unicode(str2))

def hammingdistance(str1, str2):
    pass

def smithwaterman(str1, str2):
    pass

def q_gram_tfidf_cosine_similarity(str1, str2):
    pass

def parse(nodefile, edgefile):
    with open(nodefile, "r") as f:
        l = [x.strip().split('\t') for x in f]

        for id, name in l:
            print("id = " + id, "name = " + name)

    with open(edgefile, "r") as f:
        l = [x.strip().split('\t') for x in f]

        for id1, id2 in l:
            print("id1 = " + id1, "id2 = " + id2)