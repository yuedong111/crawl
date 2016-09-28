# -*- coding: UTF-8 -*-
from scrapy.contrib.spiders import CrawlSpider  
from scrapy.selector import HtmlXPathSelector  
from cve.items import CveItem
import sys
reload(sys) 
sys.setdefaultencoding('gbk')
class DmozSpider(CrawlSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
    	"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    	"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"	
    ]
    def parse(self, response):
        
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = HtmlXPathSelector(response)
        sites = sel.select('//*[@id="site-list-content"]/div')
        items = []
        for site in sites:
            item = CveItem()
            item['title'] = site.select('div[3]/a/div/text()').extract()
            item['link'] = site.select('div[3]/a/@href').extract()
            item['desc'] = "".join(site.select('div[3]/div/text()').extract()).strip()
            items.append(item)			
        return items

