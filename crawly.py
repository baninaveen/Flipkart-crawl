from bs4 import BeautifulSoup
import requests
import subprocess
import os,sys
import time
from urlparse import urlparse

def prodfind(url):
	parsed = urlparse(url)
	parsed_url = "http://"+parsed.netloc+parsed.path
	print parsed_url
	r = requests.get(parsed_url)
	data = r.text
	soup = BeautifulSoup(data)
	
	for name in soup.find_all(itemprop="name"):
		n = name.get_text()
		#n = n.replace(',','')
		print "Name:", n
	
	for price in soup.find_all(itemprop="price"):
		p = price.get('content')
		p = p.replace(',','')
		print "Price:",int(p)
	       
	
        for img in soup.find_all(class_ ="productImage"):
		i = img.get('src')
		#n = n.replace(',','')
		print "Image: "," ",i
		break;
                
url = raw_input("Paste flipkart URL here: ")
prodfind(url)
