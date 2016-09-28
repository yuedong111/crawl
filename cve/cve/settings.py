# Scrapy settings for cve project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'cve'
BOT_VERSION = '1.0'
ITEM_PIPELINES = {'cve.pipelines.CvePipeline':700,}
SPIDER_MODULES = ['cve.spiders']
NEWSPIDER_MODULE = 'cve.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

