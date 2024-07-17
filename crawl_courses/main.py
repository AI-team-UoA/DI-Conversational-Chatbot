import scrapy

class CoursesSpider(scrapy.Spider):
    name = 'coursesspider'
    start_urls = ['https://www.di.uoa.gr/en/studies/undergraduate/courses']

    def parse(self, response):
        for tbody in response.xpath('tbody'):
            yield {
                'lesson_name': tbody.xpath('//div[@class="views-field"]/a/text()').extract()
            }
    
if __name__ == "__main__":
    cs = CoursesSpider()
    for i in range(1):
        cs.parse()