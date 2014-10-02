__author__ = 'xxdpavelxx'
import sys
import tweepy
import json
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer, KeyedProducer

consumer_key="ULI6uCZ07LS2MMGW7DVhfP9Kh"
consumer_secret="JWVLqxIqDzAMDICq7ni5WYm2sm06kNUqI465YE1Y6vhJPuJmOV"
access_key = "535814971-cHEHHJz01svTweT1KvF6HuGGtnL45O4WUVXfxgnO"
access_secret = "5FOQ8Q38p3C8Qy0CzGwJU73V5BFVVpkqmwTchVxbb3ORa"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
#file = open('today.txt', 'a')

class CustomStreamListener(tweepy.StreamListener):
    #def on_status(self, status):
     #   print status.text

    def on_data(self, data):
        try:
            json_data = json.loads(data)
            #file.write(str(json_data))
            producer.send_messages("random_topic2", str(json_data))
            print str(json_data['text'])
        except:
            pass

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
if __name__ == "__main__":
    kafka = KafkaClient("54.210.157.57:9092")
    producer = SimpleProducer(kafka)
    sapi.filter(track=['UFC'])