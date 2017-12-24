import pandas as pd
import numpy as np
import csv

def vectorizeTweets(tkntweetDB, topwordshandle):
	def getTopwords(topwordshandle):
		dct = []
		for i in range(0,20):
			with open(topwordshandle+"/topwords"+str(i)+".txt") as f:
				dct.append([])
				for line in f:
					dct[i].append(line[0:len(line)-1].lower())
		return dct

	dct = getTopwords(topwordshandle)
	with open(tkntweetDB, newline="") as f1, open("vectors/topwords." + topwordshandle + ".csv", "w") as f2:
		reader = csv.reader(f1, delimiter=" ")
		writer = csv.writer(f2, delimiter=" ")
		counter = 0
		for row in reader:
			counter += 1
			if counter % 1000 == 0:
				print(counter)

			newrow = np.zeros(20)
			length = 0
			for word in row:
				lowWord = word.lower()
				for i in range(0,20):
					if lowWord in dct[i]:
						newrow+=1
			writer.writerow(newrow)

if __name__=="__main__":
	tkntweetDB = "../data/tweet_by_ID_06_11_2017__10_30_59.txt.tknz"
	topwordshandle = "chi"
	vectorizeTweets(tkntweetDB, topwordshandle)
	tkntweetDB = "../data/us_trial.tknz"
	vectorizeTweets(tkntweetDB, topwordshandle+".trial")
