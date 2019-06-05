import scrapy

class GovDealsSpider(scrapy.Spider):
    name = "govdeals"
    start_urls = ['https://www.govdeals.com/index.cfm?fa=Main.ZipSearch&zipcode=93905&miles=150&milesKilo=miles&category=00&kWordSelect=2&locationType=miles&kWord=&country=&btn_submit=Submit']

    def parse(self, response):
        for location in response.css('table.searchResults a::attr(href)').getall():
            yield {
                'url': location
            }