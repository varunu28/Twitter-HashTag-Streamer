# Twitter-HashTag-Streamer
A Python script to stream tweets related to a Hashtag ans save it to an S3 bucket

![Demo](demo.gif)

## To-do
 - [X] Get Twitter API key
 - [X] Create streaming application to stream live tweets
 - [X] Create S3 config using boto framework
 - [X] Save every new tweet as a JSON to the S3 bucket

## How to run the  script?

 - Install the required libraries by running ```pip install -r requirements.txt``` in a virtual environment.
 - Create a Twitter application on the Twitter developer portal
 - Generate the token and and key for the application
 - Create a file ```twitter_credentials.py``` and fill the key and tokens in below template
 	```
 	ACCESS_TOKEN = ""
	ACCESS_TOKEN_SECRET = ""
	CONSUMER_KEY = ""
	CONSUMER_SECRET = ""
 	```
 - Make sure to have s3 permissions for the aws user which has been configured on your system
 - Update the hashtags and bucket name in ```config.yaml```
 - Run the script