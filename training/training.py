import pandas as pd
import numpy
import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

def loadSkipgram(filename):
	with open(filename,newline="") as f:
		reader = csv.reader(f, delimiter=' ')
		#creating column names for skip_gram data
		attributeNames = []
		for i in range(0,300):
			attributeNames.append("sk" + str(i))
		#reading
		db = []
		counter = 0
		for row in reader:
			if counter % 1000 == 0:
				print(counter)
			db.append(row)
			counter += 1
		df = pd.DataFrame(db, columns=attributeNames)
		return df

def loadLabelFile(filename):
	with open(filename,newline="") as f:
		reader = csv.reader(f)
		db = []
		for row in reader:
			db.append(row[0])
		return db

if __name__ == "__main__":
	skipgramFile = "../data/tweet_by_ID_06_11_2017__10_30_59.txt.vctr"
	labelFile = "../data/tweet_by_ID_06_11_2017__10_30_59.txt.labels"
	validateFile = "../data/us_trail.text"
	datasetName = "skipGram"
	outputPath = "../predictoins/"

	print("Loading.....")

	df = loadSkipgram(skipgramFile)
	X_train = df.values
	Y_train = loadLabelFile(labelFile)

	print("Loading finished.")

	models = []
	models.append(('KNN', KNeighborsClassifier()))
	models.append(('CART', DecisionTreeClassifier()))

	X_validate = loadValidateFile(validateFile)

	for name, model in models:
		print("Fitting: " + name)
		model.fit(X_train, Y_train)
		print("Predicting: " + name)
		predictions = moedl.predict(X_validate)
		fileName = datasetName + name + "Prediction.labels"
		with open(fileName) as f:
			writer = csv.writer(f, delimiter=" ")
			for item in predictions:
				writer.writerow([item])
