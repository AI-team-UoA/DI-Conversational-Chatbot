import scrapy
import mysql.connector

class EclassSpider(scrapy.Spider):
    name = "eclass"

    def start_requests(self):
        mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="root",
            database="DiBot"
        )
        cursor = mydb.cursor()
        query = "SELECT eclass_link FROM courses WHERE eclass_link LIKE 'https://eclass.uoa.gr/courses/%'"
        cursor.execute(query)

        links_to_visit = []

        for (eclass_link,) in cursor:
        #     code_lesson = None
        #     if eclass_link[-1] != '/':
        #         code_lesson = eclass_link.split('/')[-1]
        #     else:
        #         code_lesson = eclass_link.split('/')[-2]
            links_to_visit.append(eclass_link)

        for link in links_to_visit:
            yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        for row in response.css('.list-item'):
            announcement_link = 'https://eclass.uoa.gr' + row.css('a::attr(href)').extract_first()
            announcements_data={'announcement_link':announcement_link}
            yield scrapy.Request(announcement_link, callback=self.parse_extra_data, meta={'announcements_data': announcements_data})

    def parse_extra_data(self, response):
        announcements_data = response.meta['announcements_data']
        announcements_data['text'] = response.css('.announcement-title::text').extract_first(),
        announcements_data['date'] = response.css('.announcement-date::text').extract_first()
        return announcements_data

