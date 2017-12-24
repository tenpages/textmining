from gensim.models.keyedvectors import KeyedVectors
from nltk.corpus import wordnet



def square(x):
    return x * x


def loadSkipGram(filename):
    model = KeyedVectors.load_word2vec_format(filename)
    return model

def compute_chi():
    tweetDB = "abc.csv"
    tkntweetDB = "test.csv"
    vectorizeDB = "vectorize.csv"
    word2vecDB = "model_swm_300-6-10-low.w2v"
    word2vec = loadSkipGram(word2vecDB)
    #dataFile = "text.txt"
    #lableFile = "label.txt"
    dataFile = "tweet_by_ID_06_11_2017__10_30_59.txt.text"
    lableFile = "tweet_by_ID_06_11_2017__10_30_59.txt.labels"

    datasf = open(dataFile)
    lablesf = open(lableFile)

    cat_num = {}
    term_cat_num = {}
    terms = set()
    labels = set()
    term_chi = {}



    term_chi0 = {}
    term_chi1 = {}
    term_chi2 = {}
    term_chi3 = {}
    term_chi4 = {}
    term_chi5 = {}
    term_chi6 = {}
    term_chi7 = {}
    term_chi8 = {}
    term_chi9 = {}
    term_chi10 = {}
    term_chi11 = {}
    term_chi12 = {}
    term_chi13 = {}
    term_chi14 = {}
    term_chi15 = {}
    term_chi16 = {}
    term_chi17 = {}
    term_chi18 = {}
    term_chi19 = {}



    n = 0
    label = []

    for lineLabel in lablesf:
        lineLabel = ''.join(lineLabel).strip('\n')
        label.append(lineLabel)


    for lineText in datasf:
        lineText = lineText.replace("@", '')

        lineText = lineText.replace(".", '')

        text = lineText.split()
        #print (lineText)
        labell = label[n]
        n = n + 1
        labels.add(labell)
        #labels.add(label[n])

        if labell in cat_num:
            cat_num[labell] += 1
        else:
            cat_num[labell] = 1



    ###########################

        for term in text:
           #print(term)


           if term in word2vec.vocab:
           #if wordnet.synsets(term):

               terms.add(term)
               if term in term_cat_num:
                   if lineText in term_cat_num[term]:
                       term_cat_num[term][labell] += 1
                   else:
                       term_cat_num[term][labell] = 1
               else:
                   term_cat_num[term] = {}
                   term_cat_num[term][labell] = 1




    #print(labels)


    for word in terms:
        for label in labels:
            #print(label)

            aplusb = sum(term_cat_num[word].values())
            cplusd = n - aplusb
            a = 0
            if label in term_cat_num[word]:
                a = term_cat_num[word][label]
            else:
                continue
            b = aplusb - a
            c = cat_num[label] - a
            d = cplusd - c
            fenzi = (square(a * d - b * c) * 1.0)
            fenmu = (aplusb * cplusd)
            chi = fenzi / fenmu

            if (label == "0"):
                term_chi0[word] = chi
                print(term_chi0[word])
            elif(label == "1"):
                term_chi1[word] = chi
            elif (label == "2"):
                term_chi2[word] = chi
            elif (label == "3"):
                term_chi3[word] = chi
            elif (label == "4"):
                term_chi4[word] = chi
            elif (label == "5"):
                term_chi5[word] = chi
            elif (label == "6"):
                term_chi6[word] = chi
            elif (label == "7"):
                term_chi7[word] = chi
            elif (label == "8"):
                term_chi8[word] = chi
            elif (label == "9"):
                term_chi9[word] = chi
            elif (label == "10"):
                term_chi10[word] = chi
            elif (label == "11"):
                term_chi11[word] = chi
            elif (label == "12"):
                term_chi12[word] = chi
            elif (label == "13"):
                term_chi13[word] = chi
            elif (label == "14"):
                term_chi14[word] = chi
            elif (label == "15"):
                term_chi15[word] = chi
            elif (label == "16"):
                term_chi16[word] = chi
            elif (label == "17"):
                term_chi17[word] = chi
            elif (label == "18"):
                term_chi18[word] = chi
            elif (label == "19"):
                term_chi19[word] = chi




            if word in term_chi:
                if chi > term_chi[word]:
                    term_chi[word] = chi
            else:
                term_chi[word] = chi


    count = 0


    print(terms)
    ana = open('chi_result.txt', 'w')
    res = sorted(term_chi.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\t' + str(value) + '\n')
            count = count + 1

    count = 0


    ana = open('chi_result0.txt', 'w')
    res = sorted(term_chi0.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        #if count <= 3000:
        ana.write(key + '\t' + str(value) + '\n')
        count = count + 1

    count = 0


    ana = open('chi_result1.txt', 'w')
    res = sorted(term_chi1.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0

    ana = open('chi_result2.txt', 'w')
    res = sorted(term_chi2.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0

    ana = open('chi_result3.txt', 'w')
    res = sorted(term_chi3.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result4.txt', 'w')
    res = sorted(term_chi4.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result5.txt', 'w')
    res = sorted(term_chi5.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result6.txt', 'w')
    res = sorted(term_chi6.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result7.txt', 'w')
    res = sorted(term_chi7.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result8.txt', 'w')
    res = sorted(term_chi8.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result9.txt', 'w')
    res = sorted(term_chi9.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result10.txt', 'w')
    res = sorted(term_chi10.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result11.txt', 'w')
    res = sorted(term_chi11.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result12.txt', 'w')
    res = sorted(term_chi12.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result13.txt', 'w')
    res = sorted(term_chi13.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result14.txt', 'w')
    res = sorted(term_chi14.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result15.txt', 'w')
    res = sorted(term_chi15.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result16.txt', 'w')
    res = sorted(term_chi16.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result17.txt', 'w')
    res = sorted(term_chi17.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result18.txt', 'w')
    res = sorted(term_chi18.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0
    ana = open('chi_result19.txt', 'w')
    res = sorted(term_chi19.items(), key=lambda e: e[1], reverse=True)
    for key, value in res:
        if count <= 3000:
            ana.write(key + '\n')
            count = count + 1

    count = 0



compute_chi()

