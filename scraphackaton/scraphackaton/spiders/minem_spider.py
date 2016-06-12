import scrapy

from scraphackaton.items import ScraphackatonItem

class MinemSpider(scrapy.Spider):
    name = "minem"
    start_urls = [
        "http://www.minem.gob.pe/_noticias.php?idSector=1&pagina=" + str(n) for n in range(10)
    ]

    def parse(self, response):
        for sel in response.xpath('//a[contains(@class, "item")]'):
            item = ScraphackatonItem()
            item['title'] = sel.xpath('.//div[contains(@class, "titulo")]/text()').extract()
            item['desc'] = sel.xpath('.//div[contains(@class, "resumen")]/text()').extract()
            yield item
