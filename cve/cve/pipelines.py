# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import MySQLdb
from twisted.enterprise import adbapi
from scrapy import log
import MySQLdb.cursors
from scrapy import signals  
from scrapy.exceptions import DropItem
class CvePipeline(object):
	def __init__(self):
		self.dbpool = adbapi.ConnectionPool('MySQLdb', db='mysql',user='root', passwd='', cursorclass=MySQLdb.cursors.DictCursor,charset='utf8', use_unicode=True)

	def process_item(self,item,spider):  
		query = self.dbpool.runInteraction(self._conditional_insert, item)
	        query.addErrback(self.handle_error)
		print "lianhaole"
		return item
	def _conditional_insert(self, tx, item):
	#	for i in range(len(item['title'])):
		#	str1=str(item['title'])
		#	str2=str(item['link'])
		#	str3=str(item['desc'])
		#	sql="insert into dmoz(title,url,description) values('"+str1+"','"+str2+"','"+str3+"');"
		tx.execute("use chuli;")
		tx.execute("insert into dmoz(title,url,description) values(%s,%s,%s)",(str(item['title']),str(item['link']),str(item['desc'])))
		#	tx.execute(sql)
		print "chawanle"
		#	tx.execute("commit;")
	def handle_error(self, e):
		log.err(e)

	
        	
