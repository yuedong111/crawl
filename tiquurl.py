import os
import MySQLdb
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
				sql="insert into cve_url(cveId,Rfurl) values('"+str0+"','"+str1+"');"
				try:
					cursor.execute("use chuli;")
					cursor.execute(sql)
				except Exception,e:
					print e
			if 'ftp:' in line:
				str1=line[line.find('ftp:'):]
				sql="insert into cve_url(cveId,Rfurl) values('"+str0+"','"+str1+"');"
			#	print'str1= ',str1
				try:
                                        cursor.execute(sql)
                                except Exception,e:
                                        print e		
              	chulifile.close()
cursor.execute("commit;")
cursor.close()
conn.close()

