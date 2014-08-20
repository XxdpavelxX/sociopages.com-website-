import twitter


CONSUMER_KEY = 'CxT0uevMd2EsjqM5rNRDM9VlW'
CONSUMER_SECRET = 'u7EcEpvOVjlSjDFkfqN7gl4r1pau59I4txvPQgDOSksf5JEzw4'
OAUTH_TOKEN = '535814971-q66nrKX1BLvCQes6q8wPxwNlKvNV83DehNd5LE4M'
OAUTH_TOKEN_SECRET = 'wXeZV751OjZof5xkRVzvo7MoDLgs4t9jWVQh0ibSWrgtH'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = '#MentionSomeoneImportantForYou'   #can replace this with anything

count = 100

def lex(q):
	search_results = twitter_api.search.tweets(q=q, count=count)
	statuses = search_results['statuses']
	
	status_texts = [ status['text'] for status in statuses]

	screen_names = [user_mention['screen_name']
	for status in statuses
	for user_mention in status['entities']['user_mentions']]

	hashtags = [hashtag['text']
	for status in statuses
	for hashtag in status['entities']['hashtags']]

	#Compute a collection of all words from all tweets
	words=[w
	for t in status_texts
	for w in t.split()]
	
	return (words, screen_names, hashtags, status_texts)



# A function for computing lexical diversity
def lexical_diversity(tokens):	
	return 1.0*len(set(tokens))/len(tokens)
	
# A function for computing the average number of words per tweet
def average_words(statuses):
	total_words = sum([ len(s.split()) for s in statuses ])
	return 1.0*total_words/len(statuses)
	


if __name__=="__main__":
	words, screen_names, hashtags, status_texts=lex(q)
	print(lexical_diversity(words))
	print(lexical_diversity(screen_names))
	print(lexical_diversity(hashtags))
	#print (status_texts)
	print(average_words(status_texts))
	