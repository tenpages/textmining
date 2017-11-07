#from vectorize import tokenizeTweets
import vectorize

if __name__=="__main__":
	infile = "tweet_by_ID_06_11_2017__10_30_59.txt.text"
	outfile = "tweet_by_ID_06_11_2017__10_30_59.txt.tknz"
	vectorize.tokenizeTweets(infile, outfile)
