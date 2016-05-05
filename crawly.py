from bs4 import BeautifulSoup as bs
import requests as rq
from urlparse import urlparse

def prodfind(url):
	parsed = urlparse(url)
	parsed_url = "http://"+parsed.netloc+parsed.path
	print parsed_url
	r = rq.get(parsed_url)
	data = r.text
	soup = bs(data)
	
	for price in soup.find_all(itemprop="price"):
		p = price.get('content')
		p = p.replace(',','')
		print "Price:",int(p)
	
	for name in soup.find_all(itemprop="name"):
		n = name.get_text()
		#n = n.replace(',','')
		print "Name:", n
	
        for img in soup.find_all(class_ ="productImage"):
		i = img.get('src')
		#n = n.replace(',','')
		print "Image: ",i
		break

url = raw_input("Paste flipkart URL here: ")
prodfind(url)
