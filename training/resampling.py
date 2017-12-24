import pandas as pd
import numpy as np
import csv
from imblearn.ensemble import BalanceCascade

def loadSkipgram(filename):
	with open(filename,newline="") as f:
		reader = csv.reader(f, delimiter=' ')
		#creating column names for skip_gram data
		attributeNames = []
		for i in range(0,300):
			attributeNames.append("sk" + str(i))
		df = pd.read_csv(f, sep=' ', names=attributeNames).values
		print(df[0])
	return df

def loadLabelFile(filename):
	with open(filename,newline="") as f:
		reader = csv.reader(f)
		db = []
		for row in reader:
			db.append(row[0])
	db = np.array(db).astype(int).tolist()
	return db

def resample(X,y):
	bc = BalanceCascade(random_state=42)
	X_r, y_r = bc.fit_sample(X, y)
	print("reshape{}".format(Counter(y_r[0])))

if __name__=="__main__":
	skipgramFile = "../data/tweet_by_ID_06_11_2017__10_30_59.txt.vctr"
	labelFile = "../data/tweet_by_ID_06_11_2017__10_30_59.txt.labels"
	validateFile = "../data/us_trial.vctr"
	datasetName = "skipGram"
	#datasetName = ""
	outputPath = "../evaluation/"
	featureList = ['PRepeat', 'PSlang', 'PPositive', 'PNegative', 'NN', 'VB',
				   'JJ', 'RB', 'Non-Eng', 'SentimentScore', 'Stopwords', 'UppercaseRatio','@']

	print("Loading.....")
	print("Training set")
	X = loadSkipgram(skipgramFile)
	print("Label")
	y = loadLabelFile(labelFile)
	print(y[:10])
	print("resampling")
	resample(X,y)
