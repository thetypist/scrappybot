
# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "amarphonebook-com-css"
    start_urls = [
        'http://www.amarphonebook.com/list/Dhaka/All-Groceries/1/1113',
    ]

    def parse(self, response):
        for quote in response.css("div.list_common1"):
            yield {
                'title': quote.css("p.detailstitle > a::text").extract(),
                'phone': quote.css("p.detailsphone::text").extract(),
                'address': quote.css("p.detailsaddress::text").extract(),
                'category': quote.css("p.detailscategory > i::text").extract(),
                
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

