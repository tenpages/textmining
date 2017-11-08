from nltk.tokenize import TweetTokenizer
from gensim.models.keyedvectors import KeyedVectors
import csv

def loadSkipGram(filename):
	model = KeyedVectors.load_word2vec_format(filename)
	return model

word2vecDB = "model_swm_300-6-10-low.w2v"
word2vec = loadSkipGram(word2vecDB)
word = "fvckyao"
print(word in word2vec.vocab)