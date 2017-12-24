#imports
import csv
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import TweetTokenizer
import re


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
    #tweetlist = ['physics', 'chemistry', 1997, 2000]
    
    

    # If it becomes true then @ occur
    start = False
    with open(infile) as f1:
         

        # for all tweet
        twitterList = []
        spamreader = csv.reader(infile, delimiter=' ')
        rows = f1.readlines()
        for row in rows:
            row = row.replace(".",'')
            
            #row = "feels so lovely to be back in the can and she loves you #usa brothermerl looooooooove good bad lol @user @ Navarro College"
            tknzr = TweetTokenizer()
            text = tknzr.tokenize(row)
            tempSen = nltk.pos_tag(text)
            #print(tempSen)

            splitrow = row.split()
            #print(splitrow)
            #tweetlist = splitrow
            tweetlist = []
            length = len(splitrow)
            #print(length)

            #enumerate(row, start=0)
            for index,word in enumerate(splitrow, start=0):
                #print(word,index)
                checkPos(word)
                checkNeg(word)
                #print(word)
                #length = len(splitrow)
                #print(index)
            
            


                if((start == True) and (word != "@" )):
                    tempWord = tempWord+" "+word
                    #print(tempWord)
                    if ((start == True) and (index == length-1)):
                        judgelist = [tempWord, "@"]
                        tweetlist.append(judgelist)
                        print("#######")
    
                    #print("start t end f")
            


                elif((word == "@") and (start == True)):
                    #start = False
                    #end = True
                    judgelist = [tempWord, "@"]
                    tweetlist.append(judgelist)
                    tempWord = word
                    #print(word)

                    start = True

                elif((word == "@") and (start == False)):
                    global flagAt
                    flagAt = True
                    tempWord = word
                    start = True

                # handle # tag
               #elif(word[0] == "#"):
                #    word = word[1:]
                 #   word = word


                elif(word == "@user"):
                    print()
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
                        if(a == "NNS"):
                            # NNS and NN would be NN
                            a = "NN"
                        if(a == "VBZ"):
                            # VB and VBZ would be VB
                            a = "VB"
                        if(a == "RB"):
                            # RB would be AB
                            a = "AB"
                        if(a == "VBN"):
                            a = "VB"
                        if(a == "NNP"):
                            a = "NN"
                        if(a == "VBD"):
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
                    #b = np.append(b, judgelist)
                    #tweetlist = tweetlist.append(judgelist)
                
            # repeat feature
            if flagRepeted==True:
                judgelist = [1, "TF"]
                tweetlist.append(judgelist)
            else:
                judgelist = [0, "TF"]
                tweetlist.append(judgelist)
        
        
            # slang feature
            if flagSlang==True:
                judgelist = [1, "TF"]
                tweetlist.append(judgelist)
            else:
                judgelist = [0, "TF"]
                tweetlist.append(judgelist)

            # pos feature
            if flagPos == True:
                judgelist = [1, "TF"]
                tweetlist.append(judgelist)
            else:
                judgelist = [0, "TF"]
                tweetlist.append(judgelist)


            # neg feature
            if flagPos == True:
                judgelist = [1, "TF"]
                tweetlist.append(judgelist)
            else:
                judgelist = [0, "TF"]
                tweetlist.append(judgelist)

            # @ feature
            if flagAt == True:
                judgelist = [1, "TF"]
                tweetlist.append(judgelist)
            else:
                judgelist = [0, "TF"]
                tweetlist.append(judgelist)
        
          
            print(tweetlist)
            start = False
            iniFlag()
            
          
            twitterList.append(tweetlist)
        return twitterList
        

def iniFlag():
    global flagNeg,flagRepeted,flagSlang,flagPos,flagAt
    flagRepeted = False
    # feature2 for slang
    flagSlang = False
    # feature3 for pos
    flagPos = False
    # feature4 for neg
    flagNeg = False
    # at feature
    flagAt = False
def jstop(word):
    #stop = set(stopwords.words('english'))
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
    #print(word, "1111")

    if word != replace(word):
        #print(word,replace(word), "2222")
        
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
    #print(posWordList)
    
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

    if repl_word !=word:
        return replace(repl_word)
    else:
        return repl_word
if __name__=="__main__":
    #infile = "tweet_by_ID_06_11_2017__10_30_59.txt.tknz"
    infile = "test.txt.tknz"
    #print(replace("looooooooove"))
    judgeWords(infile)
