import pandas as pd
import numpy as np
import csv
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier

def loadSkipgram(filename):
	with open(filename,newline="") as f:
		reader = csv.reader(f, delimiter=' ')
		#creating column names for skip_gram data
		attributeNames = []
		for i in range(0,300):
			attributeNames.append("sk" + str(i))
		#reading
		df = pd.read_csv(f, sep=' ', names=attributeNames).values
		print(df[0])
	return df

def loadLabelFile(filename):
	with open(filename,newline="") as f:
		reader = csv.reader(f)
		db = []
		for row in reader:
			db.append(row[0])
	return db

def loadFeatures(featureList, handle):
	attributeNames = []
	df = pd.DataFrame()
	for i in featureList:
		with open(handle+i+'.csv',newline="") as f:
			df[i]=pd.read_csv(f,sep=' ',names=[i])
	print(df[:10])
	return df.values

def loadDescriptions(handle):
	df = pd.DataFrame()
	for i in range(0,20):
		with open(handle+str(i)+".csv", newline="") as f:
			df["des"+str(i)]=pd.read_csv(f, sep=' ', names=["des"+str(i)])
	print(df[:10])
	return df.values

def loadTopwords(handle):
	df = pd.DataFrame()
	for i in range(0,20):
		with open(handle+str(i)+".csv", newline="") as f:
			df["des"+str(i)]=pd.read_csv(f, sep=' ', names=["des"+str(i)])
	print(df[:10])
	return df.values

if __name__ == "__main__":
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
	#X_train = loadSkipgram(skipgramFile)
	handle = "../features/"
	X_train = loadFeatures(featureList,handle)
	X_train2 = loadFeatures(featureList,handle)
	X_train = np.column_stack((X_train,X_train2))
	handle = "../features/descriptions"
	X_train2 = loadDescriptions(handle)
	X_train = np.column_stack((X_train,X_train2))	

	print("Training label")
	Y_train = loadLabelFile(labelFile)

	print("Trial set")
	#X_validate = loadSkipgram(validateFile)
	handle = "../features/trial/"
	X_validate = loadFeatures(featureList,handle)
	X_validate2 = loadFeatures(featureList,handle)
	X_validate = np.column_stack((X_validate,X_validate2))
	handle = "../features/trial/descriptions"
	X_validate2 = loadDescriptions(handle)
	X_validate = np.column_stack((X_train,X_train2))	
	print("Loading finished.")

	models = []
	models.append(('RandomForest', RandomForestClassifier()))
	models.append(('ExtraTree', ExtraTreeClassifier()))
	models.append(('CART', DecisionTreeClassifier()))
	models.append(('AdaBoost', AdaBoostClassifier()))
	models.append(('GradientBoosting', GradientBoostingClassifier()))
	
	handle = ""
	for feature in featureList:
		handle += "." + feature
	handle += ".labels"

	for name, model in models:
		print("Fitting: " + name)
		model.fit(X_train, Y_train)
		print("Predicting: " + name)
		predictions = model.predict(X_validate)
		print(predictions[:10])
		print("Outputing:")
		fileName = outputPath + datasetName + name + handle
		with open(fileName, "w") as f:
			writer = csv.writer(f, delimiter=" ")
			counter = 0
			for item in predictions:
				if counter % 1000 == 0:
					print(counter)
				writer.writerow([item])
				counter += 1
