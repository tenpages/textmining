from __future__ import division

import csv
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.corpus import wordnet
from nltk.tokenize import TweetTokenizer
import re
import sys
from textblob import TextBlob

reload(sys)
sys.setdefaultencoding('utf8')
###
#  Features flag
###
# feature1 for repeat char
flagRepeted = False
# feature2 for slang
flagSlang = False
# feature3 for pos
flagPos = False
# feature4 for neg
flagNeg = False
# feature5 for @
flagAt = False

# check repeat
repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
rep1 = r'\1\2\3'

###
#  Word list
###
# pos word list
posWordList = []

# neg word list
negWordList = []

# slang list
slangList = []


def judgeWords(infile):
    # read word list
    readWordlist()
    # tweetlist = ['physics', 'chemistry', 1997, 2000]



    # If it becomes true then @ occur
    start = False
    with open(infile) as f1:

        # for all tweet
        twitterList = []
        spamreader = csv.reader(infile, delimiter=' ')
        rows = f1.readlines()
        for row in rows:
            row = row.replace(".", '')

            # row = "feels so lovely to be back in the can and she loves you #usa brothermerl looooooooove good bad lol @user @ Navarro College"
            tknzr = TweetTokenizer()
            text = tknzr.tokenize(row)
            tempSen = nltk.pos_tag(text)

            splitrow = row.split()
            # print(splitrow)
            # tweetlist = splitrow
            tweetlist = []
            length = len(splitrow)
            # print(length)

            # enumerate(row, start=0)
            for index, word in enumerate(splitrow, start=0):
                checkPos(word)
                checkNeg(word)
                # print(word)
                # length = len(splitrow)
                # print(index)




                if ((start == True) and (word != "@")):
                    tempWord = tempWord + " " + word
                    # print(tempWord)
                    if ((start == True) and (index == length - 1)):
                        judgelist = [tempWord, "@"]
                        tweetlist.append(judgelist)
                        # print("#######")

                        # print("start t end f")



                elif ((word == "@") and (start == True)):
                    # start = False
                    # end = True
                    #judgelist = [tempWord, "@"]
                    flagAt = True
                    #tweetlist.append(judgelist)
                    tempWord = word
                    # print(word)

                    start = True

                elif ((word == "@") and (start == False)):
                    global flagAt
                    flagAt = True
                    tempWord = word
                    start = True

                    # handle # tag
                    # elif(word[0] == "#"):
                    #    word = word[1:]
                    #   word = word


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

                        ###
                        # AB NN VB JJ
                        # change to four type
                        ###
                        if (a == "NNS"):
                            # NNS and NN would be NN
                            a = "NN"
                        if (a == "VBZ"):
                            # VB and VBZ would be VB
                            a = "VB"
                        if (a == "RB"):
                            # RB would be AB
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
                    # b = np.append(b, judgelist)
                    # tweetlist = tweetlist.append(judgelist)

            # repeat feature
            if flagRepeted == True:
                judgelist = [1, "FT"]
                #tweetlist.append(judgelist)
            else:
                judgelist = [0, "FT"]
                #tweetlist.append(judgelist)

            # slang feature
            if flagSlang == True:
                judgelist = [1, "FT"]
                #tweetlist.append(judgelist)
            else:
                judgelist = [0, "FT"]
                #tweetlist.append(judgelist)

            # pos feature
            if flagPos == True:
                judgelist = [1, "FT"]
                #tweetlist.append(judgelist)
            else:
                judgelist = [0, "FT"]
                #tweetlist.append(judgelist)

            # neg feature
            if flagPos == True:
                judgelist = [1, "FT"]
                #tweetlist.append(judgelist)
            else:
                judgelist = [0, "FT"]
                #tweetlist.append(judgelist)

            # @ feature
            if flagAt == True:
                judgelist = [1, "FT"]
                #tweetlist.append(judgelist)
            else:
                judgelist = [0, "FT"]
                #tweetlist.append(judgelist)

            # print(tweetlist)
            start = False
            iniFlag()

            twitterList.append(tweetlist)
        return twitterList


def iniFlag():
    global flagNeg, flagRepeted, flagSlang, flagPos, flagAt
    flagRepeted = False
    # feature2 for slang
    flagSlang = False
    # feature3 for pos
    flagPos = False
    # feature4 for neg
    flagNeg = False
    # feature5 for @
    flagAt = False


def jstop(word):
    # stop = set(stopwords.words('english'))
    stopwords = nltk.corpus.stopwords.words('english')

    if (word in stopwords):
        return True
    else:
        return False


def nonEnW(word):
    if not wordnet.synsets(word):
        # if not in word net then check if it is repeat char
        checkRepetedC(word)
        checkSlang(word)
        # check if it is slang
        return True
    else:
        return False


def checkRepetedC(word):
    # print(word, "1111")

    if word != replace(word):
        # print(word,replace(word), "2222")

        global flagRepeted
        flagRepeted = True


def checkSlang(word):
    if word in slangList:
        global flagSlang
        flagSlang = True


def checkPos(word):
    if word in posWordList:
        global flagPos
        flagPos = True


def checkNeg(word):
    if word in negWordList:
        global flagNeg
        flagNeg = True


def readWordlist():
    # read pos
    posWordTxt = open('pos_word.txt')
    lines = posWordTxt.readlines()
    global posWordList
    for line in lines:
        line = ''.join(line).strip('\n')
        posWordList.append(line)
    # print(posWordList)

    # read neg
    negWordTxt = open('neg_word.txt')
    lines = negWordTxt.readlines()
    global negWordList
    for line in lines:
        line = ''.join(line).strip('\n')
        negWordList.append(line)

    # read slang
    slangTxt = open('slang111_word.txt')
    lines = slangTxt.readlines()
    global slangList
    for line in lines:
        line = ''.join(line).strip('\n')
        slangList.append(line)


def replace(word):
    if wordnet.synsets(word):
        return word
    repl_word = repeat_regexp.sub(rep1, word)

    if repl_word != word:
        return replace(repl_word)
    else:
        return repl_word

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

def drawFeature(list):
    feature = []
    FT = []
    JJ = 0
    NN = 0
    VB = 0
    NE = 0
    ST = 0
    RB = 0
    text = ""
    tweet = ""
    NOT = 0
    negDic = ["no", "not", "never", "none", "nobody", "nothing", "neither", "nor", "nowhere", "without", "unless", "cannot", "but", ""]
    description = []
    description.append(["face", "tear", "joy", "faces", "tears", "joys"])
    description.append(["red", "heart", "hearts"])
    description.append(["smile", "face", "heart", "eye", "smiles", "faces", "hearts", "smiling", "smiled"])
    description.append(["fire", "fires"])
    description.append(["hundred", "point", "hundreds", "points"])
    description.append(["smile", "face", "eyes", "smiles", "faces", "eye", "smiled", "smiling"])
    description.append(["raise", "hand","raising", "raised", "hands"])
    description.append(["face", "blow", "kiss", "faces", "blew", "blowing", "blown", "kisses", "kissing", "kissed"])
    description.append(["christmas", "tree", "trees"])
    description.append(["two", "pink", "heart", "2", "hearts"])
    description.append(["party", "popper", "parties"])
    description.append(["loud", "cry", "face", "loudly", "crying", "cried", "faces"])
    description.append(["blue", "heart", "hearts"])
    description.append(["sparkle", "sparkles"])
    description.append(["snowflake", "snow", "snowing"])
    description.append(["smile", "face", "sunglass","smiles", "smiled", "smiling", "faces", "sunglasses"])
    description.append(["flex", "biceps"])
    description.append(["fold", "hand", "hands"])
    description.append(["ok", "hand", "hands", "okay"])
    description.append(["mouth"])
    overlap = [0 for i in range(20)]
    overlapRatio = [0.0 for i in range(20)]
    sentimentScore = 0.0
    if(list[0].child):
        node = list[list[0].child]
    else:
        print("no node in this tree")
    while(node):
        if(node.data == "NE"):
            NE += 1
            text += list[node.child].data
            tweet += list[node.child].data + " "
        elif(node.data == "ST"):
            ST += 1
            text += list[node.child].data
            tweet += list[node.child].data + " "
        elif(node.data == "FT"):
            FT.append(list[node.child].data)
        else:
            word = list[node.child].data
            pos = list[node.child + 1].data
            if(pos == "JJ"):
                JJ += 1
            elif(pos == "VB"):
                VB += 1
            elif(pos == "NN"):
                NN += 1
            elif(pos == "AB"):
                RB += 1
            else:
                print(pos + "error")
            if(negDic.count(str(word).lower()) != 0):
                NOT += 1
            for i in range(20):
                if(description[i].count(str(word).lower()) !=0):
                    overlap[i] += 1
            text += str(word)
            tweet += str(word) + " "
        if(node.sibling):
            node = list[node.sibling]
        else:
            node = None
    for i in range(20):
        overlapRatio[i] = overlap[i] / len(description[i])
    upperCase = 0
    for i in text:
        if i.isupper():
            upperCase += 1
    if(len(text) != 0):
        upperRatio = upperCase/len(text)
    else:
        upperRatio = 0.0
        for word in list:
            print (word.data)
    sentimentScore = TextBlob(tweet).sentiment.polarity
    for i in FT:
        feature.append(i)

    feature.append(NN)
    feature.append(VB)
    feature.append(JJ)
    feature.append(RB)
    feature.append(ST)
    feature.append(NE)
    feature.append(NOT)
    feature.append(upperRatio)
    feature.append(sentimentScore)
    feature.append(overlapRatio)

    return feature


if __name__=="__main__":
    #infile = "tweet_by_ID_06_11_2017__10_30_59.txt.tknz"
    infile = "test.txt"
    #infile = "tweet_test.txt.tknz"
    #print(replace("looooooooove"))
    list = judgeWords(infile)
    rootList = buildTree(list)
    featureList = []
    for root in rootList:
        feature = drawFeature(root.nodeList)
        featureList.append(feature)
    #output
    for i in range(15):
        filename = "feature" + str(i) + ".csv"
        fo = open(filename,"w")
        for j in featureList:
            fo.write(j[i])
            fo.write("\n")
        fo.close()


