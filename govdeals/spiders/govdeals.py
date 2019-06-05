import scrapy

class GovDealsSpider(scrapy.Spider):
    name = "govdeals"
    start_urls = ['https://www.govdeals.com/index.cfm?fa=Main.ZipSearch&zipcode=93905&miles=150&milesKilo=miles&category=00&kWordSelect=2&locationType=miles&kWord=&country=&btn_submit=Submit']

    def parse(self, response):
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



        for location in response.css('table.searchResults'):
            yield {
                'url': 'https://www.govdeals.com/' + location.css("a::attr(href)").extract_first(),
                'location': location.css('a::text').extract_first()
            }

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