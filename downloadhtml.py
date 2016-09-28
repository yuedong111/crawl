import os,signal
import MySQLdb
from urllib2 import urlopen
from bs4 import BeautifulSoup
from multiprocessing import Pool,Process,Queue,Lock
from mypackage.MySqlConn import Mysql
queue=Queue()
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
                                queue.put([str0,str1])

                        if 'ftp:' in line:
                                str1=line[line.find('ftp:'):]
                                queue.put([str0,str1])

                chulifile.close()
def chldhandler(signum,stackframe):
        while 1:
                try:
                        result = os.waitpid(-1,os.WNOHANG)
                except:
                        break
        signal.signal(signal.SIGCHLD,chldhandler)
 
signal.signal(signal.SIGCHLD,chldhandler)
def download(lock):
        while not queue.empty():
                mysql=Mysql()
                lock.acquire()
                try:
                       q=queue.get(timeout=0.1)
                except Exception,e:
                        print e
                finally:
                        lock.release()
                url=q[1]
                sel='use chuli;'
                try:
                        html=urlopen(url,timeout=9)
                        print 'open ok'
                        dom=BeautifulSoup(html,'lxml')
                        dom=str(dom)
                        dom=MySQLdb.escape_string(dom)
                        sql="insert into cve_rf(cveId,Rfurl,RfDetail) values('"+q[0]+"','"+q[1]+"','"+dom+"');"
                        mysql.query(sel,None)
                        mysql.query(sql,None)
                       # cursor.execute("use chuli;")
                        #cursor.execute(sql)
                except Exception,e:
                        print q[0],' has exception:',e
                        dom='the webpage cannot open'
                        sql="insert into cve_rf(cveId,Rfurl,RfDetail) values('"+q[0]+"','"+q[1]+"','"+dom+"');"
                        mysql.query(sel,None)
                        mysql.query(sql,None)
                      #  cursor.execute("use chuli;")
                       # cursor.execute(sql)
                finally:
                        mysql.dispose()
process=[]
lock=Lock()
for i in range(20):
        p=Process(target=download,args=(lock,))
        process.append(p)
        p.start()
for pr in process:
        pr.join()

