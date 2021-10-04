import scrapy
from scrapy.crawler import CrawlerProcess

class CatalogoSpider(scrapy.Spider):
    name = "catalogo"
    start_urls = [
        "https://books.toscrape.com/catalogue/page-1.html",
    ]
    custom_settings={
        'ROBOTSTXT_OBEY': True,
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def parse(self, response):
        
        for text in response.xpath("/html/body/div/div/div/div/section/div[2]/ol/li"):
            
            yield {
                'title': text.xpath("/article/h3/a/text()").get(),
                'price': text.xpath("/article/div[2]/p[1]/text()").get()
            }
        