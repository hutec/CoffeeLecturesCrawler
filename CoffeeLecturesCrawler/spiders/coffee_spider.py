import scrapy
from CoffeeLecturesCrawler.items import CoffeeLecturesCrawlerItem

class CoffeeLecturesCrawler(scrapy.Spider):
    name = "CoffeeLectures"
    start_urls = [
            "http://www.bibliothek.kit.edu/cms/coffee-lectures.php"
    ]

    def parse(self, response):
        for row in response.xpath('//tr'):
            item = CoffeeLecturesCrawlerItem()
            date = row.xpath('td[@class="cl_date"]/text()')
            item['date']    = date[0].extract() + ", " + date[1].extract().strip()
            item['title']   = row.xpath('td[@class="cl_content"]/text()').extract()
            yield item
