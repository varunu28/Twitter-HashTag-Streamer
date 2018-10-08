from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import credentials
import random
import string
import os
import boto3
import yaml

with open('config.yaml', "r") as config:
    script_config = yaml.load(config)


class TwitterStreamer():
	"""
	Class for streaming and processing live tweets
	"""

	def __init__(self):
		pass

	def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
		# Authentication logic
		listener = StdOutListener(fetched_tweets_filename)
		auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
		auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

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

			# Generating a random prefix
			random_str = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
			filename = random_str + self.fetched_tweets_filename

			with open(str(filename), 'w') as file:
				file.write(data)
			
			self.upload_to_s3(filename)

		except BaseException as e:
			print("Error: {}".format(str(e)))

		return True

	def on_error(self, status):
		print(status)

	def upload_to_s3(self, filename):
		bucket_name = script_config['bucket_name']
		output_name = str(filename)
		s3 = boto3.client('s3')

		s3.upload_file(str(filename), str(bucket_name), output_name)
		
		os.remove(str(filename))


if __name__ == "__main__":

	hash_tag_list = script_config['hash_tag_list']
	fetched_tweets_filename = script_config['fetched_tweets_filename']

	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)


	

	