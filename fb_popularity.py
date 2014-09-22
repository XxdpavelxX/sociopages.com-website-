import facebook # pip install facebook-sdk
import json

g = facebook.GraphAPI('CAACEdEose0cBAJ3ZBtQKs7WScgahjoOXVxOGXl3tXxfOZAQyVbZB3aCuudGE6v5ijaDP8WoxZCNaKkKldW0h66tJw3gr7pDVA8tkS4r0slYyNZA1G20bBT6ZAkLp9Gmq7TfuZA0P2GOZCvh1r2ddQgf6dltRzDBGDh0POyLeEMgfKechgYMwOtn1STTbFcG0BoRCk1aNrN1xQpjNnMDowgAzZAOr91dSVTtgZD')
	
# Find Pepsi and Coke in search results
#pp(g.request('search', {'q' : 'pepsi', 'type' : 'page', 'limit' : 5}))
#pp(g.request('search', {'q' : 'coke', 'type' : 'page', 'limit' : 5}))
	# Use the ids to query for likes  
#page1 = raw_input('Input name of facebook page here:')
#page2 = raw_input('input name of 2nd facebook page here:')

def popularity(page1,page2):
	# Use the ids to query for likes  
	#pp(g.get_object('40796308305'))
 
	# A quick way to format integers with commas every 3 digits
	#def int_format(n): return "{:,}".format(n)
	
	return g.get_object(page1)['likes'],g.get_object(page2)['likes']
	#+" vs "+ page2 +" likes:", int_format(g.get_object(page2)['likes'])

	
def compare(page1,page2):
	def int_format(n): return "{:,}".format(n)
	a,b=popularity(page1,page2)
		
	if a>b:
		return "%s (%s)is more popular than %s (%s)" % (page1,a,page2,b)
	elif a == b:
		return "Both pages are equally popular"
	else:
		return "%s (%s)is more popular than %s (%s)" % (page2,b,page1,a)
	
if __name__ == "__main__":
	print popularity('Megaman', 'DragonBallZ')
	print compare('Megaman', 'DragonBallZ')
	
