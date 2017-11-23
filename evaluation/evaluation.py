import pandas as pd
import numpy
import csv
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def loadLabels(filename):
	with open(filename, newline="") as f:
		reader = csv.reader(f)
		db = []
		for row in reader:
			db.append(row[0])
	return db

def evaluation(name):
	datasetName = "skipGram"
	datasetName = ""
	predFile = datasetName + name + ".PRepeat.PSlang.PPositive.PNegative.NN.VB.JJ.RB.Non-Eng.SentimentScore.Stopwords.UppercaseRatio.labels"#"Prediction.labels"
	trueFile = "../data/us_trial.labels"


	Y_validate = loadLabels(predFile)
	predictions = loadLabels(trueFile)

	with open("report_"+datasetName+name+".PRepeat.PSlang.PPositive.PNegative.NN.VB.txt", "w") as f:
		print("Dataset: " + datasetName, file=f)
		print("Method: " + name, file=f)
		print("\nAccuracy: ",accuracy_score(Y_validate, predictions), file=f)
		print("\nConfusion Matrix on 20 labels:\n",confusion_matrix(Y_validate, predictions), file=f)
		print("\nScores:\n",classification_report(Y_validate, predictions), file=f)

evaluation('CART')
evaluation('RandomForest')
evaluation('AdaBoost')
#evaluation('KNN')
