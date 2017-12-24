from __future__ import division

import nltk
from nltk.corpus import wordnet
from nltk.tokenize import TweetTokenizer
import sys
import math

reload(sys)
sys.setdefaultencoding('utf8')

def judgeWords(infile):
    start = False
    with open(infile) as f1:
        twitterList = []
        rows = f1.readlines()

        for row in rows:
            row = row.replace(".", '').lower();
            tknzr = TweetTokenizer()
            text = tknzr.tokenize(row)
            tempSen = nltk.pos_tag(text)

            splitrow = row.split()

            tweetlist = []
            length = len(splitrow)
            # print(length)


            for index, word in enumerate(splitrow, start=0):

                if ((start == True) and (word != "@")):
                    tempWord = tempWord + " " + word
                    # print(tempWord)
                    if ((start == True) and (index == length - 1)):
                        judgelist = [tempWord, "@"]
                        tweetlist.append(judgelist)

                elif ((word == "@") and (start == True)):

                    tempWord = word

                    start = True

                elif ((word == "@") and (start == False)):
                    tempWord = word
                    start = True




                elif (word == "@user"):
                    pass
                    # do not add to list

                else:
                    if jstop(word):
                        a = "ST"
                    elif nonEnW(word):
                        a = "NE"
                    else:
                        a = tempSen[index][1]


                        if (a == "NNS"):
                            a = "NN"
                        if (a == "VBZ"):
                            a = "VB"
                        if (a == "RB"):
                            a = "AB"
                        if (a == "VBN"):
                            a = "VB"
                        if (a == "NNP"):
                            a = "NN"
                        if (a == "VBD"):
                            a = "VB"
                        if (a == "VBP"):
                            a = "VB"
                        if (a == "CD"):
                            a = "NN"
                        if (a == "JJR"):
                            a = "JJ"
                        if (a == "VBG"):
                            a = "VB"
                        if (a == "JJS"):
                            a = "JJ"

                    judgelist = [word, a]
                    tweetlist.append(judgelist)

            start = False

            twitterList.append(tweetlist)
        return twitterList

def jstop(word):

    stopwords = nltk.corpus.stopwords.words('english')

    if (word in stopwords):
        return True
    else:
        return False


def nonEnW(word):
    if not wordnet.synsets(word):

        return True
    else:
        return False

class TreeNode:


    def __init__(self, word):
        self.data = word
        self.child = None
        self.sibling = None

class Tree:
    def __init__(self, list):
        nodeCount = 0


        self.nodeList = []
        node = TreeNode("root")
        self.nodeList.append(node)
        tmpEnd = nodeCount
        tmpStart = nodeCount + 1

        for word in list:

            if(word[1] == "ST" or word[1] == "NE" or word[1] == "FT"):
                self.nodeList.append(TreeNode(word[1]))
                nodeCount += 1
                if(tmpEnd == 0):
                    self.nodeList[tmpEnd].child = nodeCount
                else:
                    self.nodeList[tmpStart].sibling = nodeCount
                self.nodeList.append(TreeNode(word[0]))
                nodeCount += 1
                self.nodeList[nodeCount - 1].child = nodeCount

            elif(word[1] == "NN" or word[1] == "AB" or word[1] == "JJ" or word[1] == "VB"):
                self.nodeList.append(TreeNode("EW"))
                nodeCount += 1
                tmp = nodeCount
                if (tmpEnd == 0):
                    self.nodeList[tmpEnd].child = nodeCount
                else:
                    self.nodeList[tmpStart].sibling = nodeCount
                self.nodeList.append(TreeNode(word[0]))
                nodeCount += 1
                self.nodeList[tmp].child = nodeCount
                self.nodeList.append(TreeNode(word[1]))
                nodeCount += 1
                self.nodeList[nodeCount - 1].sibling = nodeCount
            else:
                continue

            tmpStart = tmpEnd + 1
            tmpEnd = nodeCount

def buildTree(list):
    rootList = []
    for tweet in list:
        rootList.append(Tree(tweet))
    print("build success")
    return rootList

if __name__ == "__main__":
    infile = "tweet_by_ID_06_11_2017__10_30_59.txt.tknz"
    label_infile = "tweet_by_ID_06_11_2017__10_30_59.txt.labels"
    #infile = "us_tria.tknz"
    #label_infile = "us_trial.tknz"
    wordlist = judgeWords(infile)
    label_list = []
    with open(label_infile) as f1:
        rows = f1.readlines()
        for row in rows:
            label_list.append(int(row))
    list = []
    rootList = buildTree(wordlist)
    for i in range(21):
        dict = {}
        list.append(dict)
    count = 0
    for root in rootList:
        key = label_list[count]
        dict = list[key]
        dict2 = list[20]
        count += 1
        if(root.nodeList[0].child != None):
            node = root.nodeList[root.nodeList[0].child]
        else:
            node = None
        while(node):
            if(node.data == "ST"):
                pass
            elif(node.data == "NE" or node.data == "EW"):
                word = root.nodeList[node.child].data
                if(dict.has_key(word)):
                    list[key][word] += 1
                else:
                    list[key][word] = 1
                if(dict2.has_key(word)):
                    list[20][word] += 1
                else:
                    list[20][word] = 1
            if (node.sibling):
                node = root.nodeList[node.sibling]
            else:
                node = None
    nList = []
    for i in range(21):
        dict = list[i]
        dict = sorted(dict.items(), key=lambda item:item[1], reverse=True)
        nList.append(dict)
    k=300
    count = 0
    filename = "tf_topwords"
    for dict in nList:
        if(count == 20):
            k=1000
        count += 1
        filename += str(nList.index(dict)) + ".txt"
        fo = open(filename, "w")
        for i in range(k):
            if (len(dict) > i):
                fo.write(str(dict[i][0]))
                fo.write("\n")
        fo.close()
        filename = "tf_topwords"
    fo.close()
    for dict in list:
        tfcount = 0
        for k in dict:
            tfcount += dict[k]
        for k in dict:
            idfcount = 0
            for dict1 in list:
                if dict1.has_key(k):
                    idfcount += 1
                else:
                    pass
            idf = math.log(20/idfcount)
            dict[k] = (dict[k]/tfcount) * idf
    newList = []
    for i in range(21):
        dict = list[i]
        dict = sorted(dict.items(), key=lambda item:item[1], reverse=True)
        newList.append(dict)
    k = 300
    count = 0
    filename = "tfidf_topwords"
    for dict in newList:
        if(count == 20):
            k = 1000
        count += 1
        filename += str(newList.index(dict)) + ".txt"
        fo = open(filename, "w")
        for i in range(k):
            if(len(dict) > i):
                fo.write(str(dict[i][0]))
                fo.write("\n")
        fo.close()
        filename = "tfidf_topwords"
    fo.close()