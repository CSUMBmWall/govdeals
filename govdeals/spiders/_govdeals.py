import scrapy
from urllib.parse import urljoin

class GovDealsSpider(scrapy.Spider):
    open('govdeals.json', 'w').close()
    name = "govdeals"
    start_urls = ['https://www.govdeals.com/index.cfm?fa=Main.ZipSearch&zipcode=93905&miles=150&milesKilo=miles&category=00&kWordSelect=2&locationType=miles&kWord=&country=&btn_submit=Submit']
    domain = "https://www.govdeals.com/"

    def parse(self, response):
        domain = "https://www.govdeals.com/"
        for location in response.xpath('//table[@class="searchResults"]/tr'):
            # yield {
            #     'url': location.css("a::attr(href)").get(),
            #     'location': location.css('a::text').get()                
            # }
            yield {
                # 'value': location.css("a::attr(href)").get(),
                'url': urljoin(domain, location.css("a::attr(href)").get()),
                'location': str(location.css('a::text').get())                
            }


            # for deal in deals:
            url = location.css("a::attr(href)").get()
            if url is not None:
                next_page = urljoin(domain, url)
                yield scrapy.Request(next_page, callback=self.parseDetails)

    def parseDetails(self, response):
        domain = "https://www.govdeals.com/"
        for detail_location in response.xpath('//table[@class="searchResults"]/tr'):
            # yield {
            #     'img': location.css("img::attr(src)"),
            #     'desc': location.css("img::text"),
            #     # 'url': location.xpath("//div/a/@href")
            # }
            yield {
                # 'value': location.css("a::attr(href)").get(),
                'url': urljoin(domain, detail_location.css("a::attr(href)").get()),
                'title': detail_location.css('a::attr(title)').get(),
                'img': detail_location.xpath('//a/img/@src')               
            }


            # for deal in deals:
            url = detail_location.css("a::attr(href)").get()
            if url is not None:
                next_page = urljoin(domain, url)
                yield scrapy.Request(next_page, callback=self.parse)


        # loc_urls = []
        # for location in response.css('table.searchResults a::attr(href)').getall():
        #     yield loc_urls.append('https://www.govdeals.com/' + location),
        #     print(location)

        # locations = []
        # for location in response.css('table.searchResults a::text').getall():
        #     yield locations.append(location)



        # filename = 'deals.txt'
        # with open(filename, 'wb') as f:
        #     f.write("\n".join(loc_urls))
        #     f.write("\n".join(locations))




        # loc_urls = []
        # for location in response.css('table.searchResults a::attr(href)').getall():
        #     loc_urls.append('https://www.govdeals.com/' + location)
        #     # print(loc_urls.append('https://www.govdeals.com/' + location))

        # locations = []
        # for location in response.css('table.searchResults a::text').getall():
        #     locations.append(location)
        #     # print(locations.append(location))

        # return loc_urls, locations

        # filename = 'deals.txt'
        # with open(filename, 'wb') as f:
        #     f.write("\n".join(loc_urls))
        #     f.write("\n".join(locations))



        

        # for location in response.css('table.searchResults a::text').getall():
        #     yield {
        #         'location': location
        #     }

    # def parse(self, response):
    #     for listing in response.css('table.searchResults').getall():
    #         yield {
    #             'url': listing.css('a::attr(href)'),
    #             'location': listing.css('a::text')
    #         }

    # xpath table = response.xpath('//*[@class="searchResults"]//a//@href')