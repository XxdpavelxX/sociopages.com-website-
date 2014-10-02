__author__ = 'xxdpavelxx'
#6.3,6.5,6.6,6.7,11.1 python cookbook

import requests
import feedparser
from htmlParser import MyHTMLParser
import lxml
from lxml import etree, objectify
from io import StringIO, BytesIO
#from pymongo import MongoClient

#c = MongoClient("localhost", 27017)
#db= c.cikdb


#cik= raw_input('Please enter a CIK number:' )   Note: If you bring this back, bring back link var on line 71
#print cik


#return sec page url
#parameter is cik number
def getLatestFiling( cik, filingType="13F-HR"):
    payload = {'CIK': cik,'action':'getcompany','type':"","dateb":"","owner":"exclude","start":"0","count":40,"output":'atom'}
    r = requests.get("http://www.sec.gov/cgi-bin/browse-edgar", params=payload)
    feed = feedparser.parse(r.text)
    for entry in feed['entries']:
        #print 'test'+entry.title
        if '13F-HR' in entry.title:
            return entry.link
    return "No filing found, please try a different CIK number."
    #return ""

#returns link to sec filing text file
#parameter - sec page url
def getFilingTextFile(secPageUrl):
    parser = MyHTMLParser()
    r = requests.get(secPageUrl)
    parser.feed(r.text)
    return 'http://www.sec.gov'+parser.linkToTextFile

# return dictionary of holding and % of holdings
def getHoldings(linkToTextFile):
    #collection = db.linkToTextFile
    #print linkToTextFile
    r = requests.get(linkToTextFile)
    XMLer= str(r.text.replace('&', '&amp;'))
    #print XMLer
    start= XMLer.find('<informationTable')
    end= XMLer.find('</informationTable>')
    a= XMLer[start:end+19]  #string type

    lxml_form = etree.fromstring(a)
    #print type(lxml_form)

    for child in lxml_form.getiterator():
        if not hasattr(child.tag, 'find'): continue  # (1)
        i = child.tag.find('}')
        if i >= 0:
            child.tag = child.tag[i+1:]
        if 'nameOfIssuer' in child.tag:
            #collection.insert({child.tag:child.text})
            yield child.tag + " : " + child.text
        if 'value' in child.tag:
            #collection.insert({child.tag:child.text})
            yield child.tag + ' : ' + child.text
            #yield ('--------------------------------------------------------------------------------------------')
#getLatestFiling('0001166559', filingType="13F-HR")


    #print #lxml.etree.XTMl(a)
    #root = etree.fromstring(r.text.replace('&', '&amp;'))
    #print root

#bad sik= 0000002110

#cik='0001166559'
#link=getLatestFiling(cik)  Note: If you bring this back, bring back cik var on line 11!

#if link!="No filing found, please try a different CIK number.":
#    filingLink=getFilingTextFile(link)
#    getHoldings(filingLink)



#print getFilingTextFile(h)



