from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer, KeyedProducer
from pymongo import MongoClient
import json
import ast

c = MongoClient("localhost", 27017)
db = c.twitter
collection = db.tweets

kafka = KafkaClient("54.210.157.57:9092")
consumer = SimpleConsumer(kafka,"anygroup??","random_topic2")  #(kafka, ??? collection, topic)
def tweet_mongo():
	for tweet in consumer:
	# print tweet.message.ry:
		try:
			jsonTweet=json.dumps(tweet.message.value)
			jsonLoad=json.loads(jsonTweet)
			Jdict= ast.literal_eval(jsonLoad)
			collection.insert(Jdict)
			print Jdict['text']

		except:
			pass
			
if __name__ == '__main__':			
	tweet_mongo()
