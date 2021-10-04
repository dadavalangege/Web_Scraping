import scrapy
from scrapy.crawler import CrawlerProcess

class CatalogoSpider(scrapy.Spider):
    name = "catalogo"
    page_number = 2
    start_urls = [
        "https://books.toscrape.com/catalogue/page-1.html",
    ]
    custom_settings={
        'ROBOTSTXT_OBEY': True,
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def parse(self, response):
        books = response.css('article.product_pod')
        titles = books.css('h3 a::text').extract()
        prices = books.css('p.price_color::text').extract()
        yield {
            'title': titles,
            'price': prices
        }

        next_page = 'https://books.toscrape.com/catalogue/page-' + str(CatalogoSpider.page_number) + '.html'
        if CatalogoSpider.page_number <= 20:
            CatalogoSpider.page_number +=1
            yield response.follow(next_page, callback = self.parse)