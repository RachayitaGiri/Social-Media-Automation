import bson
import pymongo
from pymongo import MongoClient
import re


client = MongoClient()
db = client.test
coll = db.newtweets

# open a file in which you want to dump the data from the bson collection
# HERE

try:
	data = coll.find()
	print "Records found."
	for row in data:
		#regex to find RT at the beginning of tweet; match() returns NONE if match is not found.
		match = re.match(r'(^RT)',row['text'])
		#So if match is not found, i.e. the tweet is not a retweet then print the tweet
		if(match == None):
			print row['text'] 
			'''Instead of printing the text on the standard output, print it in the json file you opened earlier
			that would be all
			Add some columns and extra information if you will need. Such as metadata and all in the json file
			You can also parse the bson collection completely and record all columns instead of just the text
			To access the data organization, refer to the "db.json/test/newtweets.metadata.json" file
			mylist = row['entities']['user_mentions']
			for user in mylist:
				print user['id']
			'''

except Exception, e:
	print str(e)