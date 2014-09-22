__author__ = 'xxdpavelxx'
from HTMLParser import HTMLParser
import requests
import re

# create a subclass and override the handler methods

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        #print "Encountered a start tag:", tag
        if tag=='a':
            for attr in attrs:
               #getting href value from attr tuple
               href= (attr[1])
               # find if href match regular expression
               links = re.findall(r'[\D]+/[\D]+/[\D]+/[0-9]+/[0-9]+/[0-9]+-[0-9]+-[0-9]+.txt',href)
               if len(links)==1: # array holding all found links
                  self.linkToTextFile = links[0]

    #def handle_endtag(self, tag):
        #print "Encountered an end tag :", tag
    #def handle_data(self, data):
        #if (data=='Complete submission text file'):
            #print "Encountered some data  :", data

parser = MyHTMLParser()
r = requests.get("http://www.sec.gov/Archives/edgar/data/1166559/000104746907006532/0001047469-07-006532-index.htm")
parser.feed(r.text)
print 'www.sec.gov'+parser.linkToTextFile
