#-*- coding: UTF-8 -*-
import os
import MySQLdb
conn=MySQLdb.Connection(host="localhost",user="root",passwd="",db="mysql",charset="UTF8")
cursor=conn.cursor()
files=os.listdir(os.getcwd())
for file1 in files:
	if '.txt'in file1:
		chulifile=open(file1,'r')
		lines=chulifile.readlines()
		str1=""
		str2=""
		flag=True
		for i in range(len(lines)):
			if 'Name: CVE-'in lines[i]:
	                	str0=lines[i][5:]
   		     	elif 'Description:'in lines[i]:
				while(flag==True):
					str1+=lines[i]
					i=i+1
					if 'NOTE:'in lines[i] or'::'in lines[i]:
						str1+=lines[i]
						i=i+1
					elif 'Status:'in lines[i]:
						j=i
						flag=False
					elif ':'in lines[i]:
                                                j=i
                                                flag=False
	        for i in range(j,len(lines)):
			if 'Name: CVE-'not in lines[i]:
				str2+=lines[i]
		if(str0==''):
			str0="lastitem"
		str0=str0.strip()
		if'me:'in str0:
                        str0=str0[3:]
		if'e:'in str0:
			str0=str0[2:]
		if':'in str0:
                        str0=str0[1:]
		str0=MySQLdb.escape_string(str0)
		str1=MySQLdb.escape_string(str1)
		str2=MySQLdb.escape_string(str2)
		sql="insert into cve(CveID,Description,Reference) values('"+str0+"','"+str1+"','"+str2+"');"
#		print sql
		try:
			cursor.execute("use chuli;")
			cursor.execute(sql)
		except Exception,e:
			print e
		chulifile.close()
cursor.execute("commit;")
cursor.close()
conn.close()
