# Twitter-HashTag-Streamer
A Python script to stream tweets related to a Hashtag ans save it to an S3 bucket

## To-do
 - [X] Get Twitter API key
 - [X] Create streaming application to stream live tweets
 - [ ] Create S3 config using boto framework
 - [ ] Save every new tweet as a JSON to the S3 bucket

## How to run the  script?

 - Create a Twitter application on the Twitter developer portal
 - Generate the token and and key for the application
 - Create a file ```twitter_credentials.py``` and fill the key and tokens in below template
 	```
 	ACCESS_TOKEN = ""
	ACCESS_TOKEN_SECRET = ""
	CONSUMER_KEY = ""
	CONSUMER_SECRET = ""
 	```
 - Run the script