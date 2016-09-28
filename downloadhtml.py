import os
import MySQLdb
from urllib2 import urlopen
from bs4 import BeautifulSoup
from multiprocessing import Pool,Process,Queue
#conn=MySQLdb.Connection(host="localhost",user="root",passwd="",db="chuli",charset="UTF8")
#cursor=conn.cursor()
def download(queue,wgt):
	print 'bengin'
        while not queue.empty():
                q=queue.get()
                url=q[1]
                print q[0]
                try:
                        html=urlopen(url,timeout=10)
                        print 'open ok'
                        dom=BeautifulSoup(html,'lxml')
                        dom=str(dom)
                        dom=MySQLdb.escape_string(dom)
#                       sql="insert into cve_rf(cveId,Rfurl,RfDetail) values('"+q[0]+"','"+q[1]+"','"+dom+"');"
#                       cursor.execute("use chuli;")
#                       cursor.execute(sql)
#                       cursor.execute("commit;")
                except Exception,e:
                        print q[0],' has exception:',e
                        dom='the webpage cannot open'
#                       sql="insert into cve_rf(cveId,Rfurl,RfDetail) values('"+q[0]+"','"+q[1]+"','"+dom+"');"
#                       cursor.execute("use chuli;")
#                       cursor.execute(sql)
#                       cursor.execute("commit;")
                content=(q[0],q[1],dom)
                wgt.append(content)
		return wgt
#process=[]
#for i in range(5):
#       p=Process(target=download)
#       process.append(p)
#       p.start()
#for pr in process:
#       pr.join()
#cursor.close()
#conn.close()
def main():
	queue1=Queue()
	files=os.listdir(os.getcwd())
	for wenjian in files:
		if '.txt' in wenjian:
			chulifile=open(wenjian,'r')
			lines=chulifile.readlines()                          
			for line in lines:
				if 'Name: CVE-' in line:
                        	    	str0=line[line.find('Name: CVE-')+6:]
			for line in lines:
				if 'http:' in line:
					str1=line[line.find('http:'):]
					try:
						queue1.put([str0,str1])
					except Exception,e:
						print e
					if queue1.empty():
						print 'empyty111'
				if 'ftp:' in line:
					str1=line[line.find('ftp:'):]
					queue1.put([str0,str1])
         	     	chulifile.close()
	wgt=[]
	wgt=download(queue1,wgt)
	print wgt
if __name__ == '__main__':
	main()
