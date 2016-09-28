from urllib2 import urlopen
from bs4 import BeautifulSoup
print '000'
try:
	html = urlopen("http://www.securityfocus.com/bid/61",timeout=5)
	print '111'
	html=BeautifulSoup(html,'lxml')
	html=str(html)
	print html
except Exception,e:
	print e
	html='html null'
	print "error"
	print html
