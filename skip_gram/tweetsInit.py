from nltk.tokenize import TweetTokenizer
from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import csv

def tokenizeTweets(infile, outfile):
	tknzr = TweetTokenizer()
	with open(infile) as f1, open(outfile, "w") as f2:
		writer = csv.writer(f2, delimiter=" ")
		row = f1.readline()
		while row:
			tkns = tknzr.tokenize(row)
			writer.writerow(tkns)
			row = f1.readline()

def vectorizeTweets(tkntweetDB, vectorizeDB, word2vecDB):
	def loadSkipGram(filename):
		model = KeyedVectors.load_word2vec_format(filename)
		return model

	word2vec = loadSkipGram(word2vecDB)
	with open(tkntweetDB, newline="") as f1, open(vectorizeDB, "w") as f2:
		reader = csv.reader(f1, delimiter=" ")
		writer = csv.writer(f2, delimiter=" ")
		counter = 0
		for row in reader:
			counter += 1
			if counter % 1000 == 0:
				print(counter)
			newrow = np.zeros(300)
			length = 0
			for word in row:
				lowWord = word.lower()
				if lowWord in word2vec.vocab:
					newrow += word2vec.word_vec(lowWord)
					length += 1
			if length!=0:
				newrow /= length
			writer.writerow(newrow)

if __name__=="__main__":
	#tweetDB = "tweet_by_ID_06_11_2017__10_30_59.txt.text"
	#tkntweetDB = "tweet_by_ID_06_11_2017__10_30_59.txt.tknt"
	tweetDB = "abc.csv"
	tkntweetDB = "test.csv"
	vectorizeDB = "vectorize.csv"
	word2vecDB = "model_swm_300-6-10-low.w2v"

	tokenizeTweets(tweetDB, tkntweetDB)
	vectorizeTweets(tkntweetDB, vectorizeDB, word2vecDB)
