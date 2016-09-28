import os
import MySQLdb
from urllib2 import urlopen
from bs4 import BeautifulSoup
conn=MySQLdb.Connection(host="localhost",user="root",passwd="",db="chuli",charset="UTF8")
cursor=conn.cursor()
files=os.listdir(os.getcwd())
for wenjian in files:
	if '.txt' in wenjian:
		chulifile=open(wenjian,'r')
		lines=chulifile.readlines()                          
		for line in lines:
			if 'Name: CVE-' in line:
                            	str0=line[line.find('Name: CVE-')+6:]
                        #	print 'str0= ',str0
		for line in lines:
			if 'http:' in line:
				str1=line[line.find('http:'):]
			#	print'str1= ',str1
				try:
					html=urlopen(str1,timeout=5)
					dom=BeautifulSoup(html,'lxml')
					dom=str(dom)
					dom=MySQLdb.escape_string(dom)
					sql="insert into cve_rf(cveId,Rfurl,RfDetail) values('"+str0+"','"+str1+"','"+dom+"');"
					cursor.execute("use chuli;")
					cursor.execute(sql)
				except Exception,e:
					print e
					dom='the webpage cannot open'
					sql="insert into cve_rf(cveId,Rfurl,RfDetail) values('"+str0+"','"+str1+"','"+dom+"');"
                                        cursor.execute("use chuli;")
                                        cursor.execute(sql)
			if 'ftp:' in line:
				str1=line[line.find('ftp:'):]
				try:
                                        html=urlopen(str1,timeout=5)
                                        dom=BeautifulSoup(html,'lxml')
					dom=str(dom)
					dom=MySQLdb.escape_string(dom)
                                        sql="insert into cve_rf(cveId,Rfurl,RfDetail) values('"+str0+"','"+str1+"','"+dom+"');"
                                        cursor.execute("use chuli;")
                                        cursor.execute(sql)
                                except Exception,e:
                                        dom='the webpage cannot open'
                                        sql="insert into cve_rf(cveId,Rfurl,RfDetail) values('"+str0+"','"+str1+"','"+dom+"');"
                                        cursor.execute("use chuli;")
                                        cursor.execute(sql)				
              	chulifile.close()
cursor.execute("commit;")
cursor.close()
conn.close()

