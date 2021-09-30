import scrapy
from scrapy.crawler import CrawlerProcess

class CatalogoSpider(scrapy.Spider):
    name = "catalogo"
    start_urls = [
        'https://www.macba.cat/es/buscador/tipo/exposicion?key=&page=0',
    ]

    def parse(self, response):
        for title in response.css('div.snippet_title'):
            yield {
                title.css('div::text').get()
                
                #'title': title.css('span.text::text').get(),
                #'author': quote.css('span small::text').get(),
                #'tags': quote.css('div.tags a.tag::text').getall(),
            }
        #next_page = response.css('li.next a::attr(href)').get()
        #if next_page is not None:
            #yield response.follow(next_page, callback=self.parse)