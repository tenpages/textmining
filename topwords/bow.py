import pandas as pd
import numpy as np
import csv

def vectorizeTweets(tkntweetDB, topwordshandle, trial=""):
	def getTopwords(topwordshandle):
		dct = {}
		with open(topwordshandle+"/topwords"+".txt") as f:
			counter = 0
			for line in f:
				dct[line[0:len(line)-1].lower()]=counter
				counter += 1
		return dct

	dct = getTopwords(topwordshandle)
	with open(tkntweetDB, newline="") as f1, open("bow/bow." + trial + topwordshandle + ".csv", "w") as f2:
		reader = csv.reader(f1, delimiter=" ")
		writer = csv.writer(f2, delimiter=" ")
		counter = 0
		for row in reader:
			counter += 1
			if counter % 1000 == 0:
				print(counter)

			newrow = np.zeros(1000)
			length = 0
			for word in row:
				lowWord = word.lower()
				if dct.__contains__(lowWord):
					newrow[dct[lowWord]] +=1
			writer.writerow(newrow)

if __name__=="__main__":
	tkntweetDB = "../data/tweet_by_ID_06_11_2017__10_30_59.txt.tknz"
	topwordshandle = "tf.new"#"tf.new, tfidf.new"
	vectorizeTweets(tkntweetDB, topwordshandle)
	tkntweetDB = "../data/us_trial.tknz"
	vectorizeTweets(tkntweetDB, topwordshandle, trial="trial.")
