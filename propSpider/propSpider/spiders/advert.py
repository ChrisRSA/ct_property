from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class AdvertSpider(CrawlSpider):
    name = 'adverts'
    allowed_domains = ['privateproperty.co.za']
    start_urls = ['https://www.privateproperty.co.za/for-sale']
    rules =[Rule(LinkExtractor(allow=r'/western-cape/cape-town/.*'), callback='parse_items', follow=True)]

    def parse_items(self,response):
        url = response.url
        #title = response.css('h1::text').extract_first()
        #price = response.css('span#detailsPrice::text').extract_first()
        print('URL is: {}'.format(url))
        #print('Title is: {}'.format(title))
        #print('Price is: {}'.format(price))
