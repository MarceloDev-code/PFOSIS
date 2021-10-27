import scrapy
import csv


class FondosConcursablesSpider(scrapy.Spider):
    name = 'fondos_concursables'
    with open("fondos.csv","r") as f:
        reader = csv.DictReader(f)
        start_urls = [item['link'] for item in reader]

    def parse(self, response):
        yield {"link":response.url}

    def parse(self, response):
        pass
