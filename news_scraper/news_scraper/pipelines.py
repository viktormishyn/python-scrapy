# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exceptions import DropItem
from datetime import datetime


class CheckItemPipeline:
    def process_item(self, article, spider):
        if not all([article['url'],
                    article['source'],
                    article['title'],
                    article['description'],
                    article['body'],
                    article['author'],
                    article['datePublished']]):
            raise DropItem('Missing something')
        return article


class CleanAuthorPipeline:
    def process_item(self, article, spider):
        article['author'] = article['author'].replace(', CNN', '').strip()
        return article
