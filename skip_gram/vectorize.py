from nltk.tokenize import TweetTokenizer
import csv

def tokenizeTweets(infile, outfile):
	tknzr = TweetTokenizer()
	with open(infile, newline="") as f1, open(outfile, "w") as f2:
		reader = csv.reader(f1, delimiter=" ")
		writer = csv.writer(f2, delimiter=" ")
		for row in reader:
			tkns = tknzr.tokenize(row[0])
			writer.writerow(tkns)

def loadSkipGram(filename):
	with open(filename, newline="") as f:
		reader = csv.reader(f, delimiter=" ")
		skipGramVector = []
		skipGramVocabulary = []
		for row in reader:
			#skipGramVocabulary.append(row[0])
			skipGramVector.append(row[1:])
		return skipGramVector, skipGramVocabulary

def embeddingTweets(tkntweetDB, embeddingDB):
	with open(tkntweetDB, newline="") as f1, open(embeddingDB, "w") as f2:
		reader = csv.reader(f1, delimiter=" ")
		writer = csv.writer(f2, delimiter=" ")
		for row in reader:
			newrow = []
			for word in row:
				if word in skipGramVocabulary:
					newrow.append(skipGramVocabulary.index(word))

tweetDB = "abc.csv"
tkntweetDB = "test.csv"
skipGramDB = "skipGram.csv"
tokenizeTweets(tweetDB, tkntweetDB)
skipGramVector, skipGramVocabulary = loadSkipGram(skipGramDB)
embeddingTweets(tkntweetDB, embeddingDB)