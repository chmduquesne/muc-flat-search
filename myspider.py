import scrapy

class ImmobilienScout24Spider(scrapy.Spider):
    name = 'ImmobilienScout24Spider'
    start_urls = [
            'https://www.immobilienscout24.de/Suche/S-T/Wohnung-Miete/Bayern/Muenchen'
            ]

    def parse(self, response):
        # loop over articles
        for article in response.xpath("//article"):
            yield response.follow(article.xpath(".//a")[0], self.parse_article)

        ## find next page
        #next_page = response.xpath("//div[@id='pager']//a")[-1]
        #yield response.follow(next_page)


    def parse_article(self, r):
        details = r.xpath("//div[@class='is24-ex-details']")
        print {
            "url": r.url,
            "title": r.xpath("//h1[@id='expose-title']/text()")
                .extract_first(),
            "zipcode": r.xpath(
                "//span[@class='zip-region-and-country']/text()")
                .extract_first(),
            "price": details.xpath(".//dt[@class='is24qa-gesamtmiete']/text()")
                .extract_first(),
        }
