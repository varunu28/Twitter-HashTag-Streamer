from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


class TwitterStreamer():
	"""
	Class for streaming and processing live tweets
	"""

	def __init__(self):
		pass

	def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
		# Authentication logic
		listener = StdOutListener(fetched_tweets_filename)
		auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
		auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

		stream = Stream(auth, listener)

		stream.filter(track=hash_tag_list)


class StdOutListener(StreamListener):
	"""
	Basic listener class that just prints received tweets to console
	"""
	
	def __init__(self, fetched_tweets_filename):
		self.fetched_tweets_filename = fetched_tweets_filename

	def on_data(self, data):
		try:
			print(data)
			with open(self.fetched_tweets_filename, 'a') as file:
				file.write(data)
		except BaseException as e:
			print("Error: {}".format(str(e)))

		return True

	def on_error(self, status):
		print(status)


if __name__ == "__main__":

	hash_tag_list = ['#cmpe295A']
	fetched_tweets_filename = "tweets.json"

	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)


	

	