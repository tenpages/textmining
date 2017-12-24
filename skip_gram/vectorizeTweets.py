from tweetsInit import vectorizeTweets

if __name__=="__main__":
	infile = "tweet_by_ID_06_11_2017__10_30_59.txt.tknz"
	outfile = "tweet_by_ID_06_11_2017__10_30_59.txt.vctr"
	word2vecDB = "model_swm_300-6-10-low.w2v"

	vectorizeTweets(infile, outfile, word2vecDB)

