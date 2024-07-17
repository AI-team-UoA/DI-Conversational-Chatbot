import scrapy

class CoursesSpider(scrapy.Spider):
    name = 'coursesspider'
    start_urls = ['https://www.di.uoa.gr/en/studies/undergraduate/courses']

    def parse(self, response):
        for row in response.css('tbody tr'):
            course_link = 'https://www.di.uoa.gr' + row.css('a::attr(href)').extract_first()
            initial_courses_data = {
                'name': row.css('a::text').extract_first(),
                'code': row.css('.views-field.views-field-field-course-code::text').extract_first(),
                'ects': row.css('.views-field.views-field-field-course-ects::text').extract_first(),
                'type': row.css('.views-field.views-field-field-course-type::text').extract_first(),
                'link': course_link
            }
            yield scrapy.Request(course_link, callback=self.parse_extra_data, meta={'initial_courses_data': initial_courses_data})

    def parse_extra_data(self, response):
        initial_courses_data = response.meta['initial_courses_data']
        initial_courses_data['semester'] = response.css('div.views-field.views-field-field-undegraduate-course-semest div.field-content::text').extract_first()
        initial_courses_data['theory_class_hours'] = response.css('div.views-field.views-field-field-course-hours div.field-content::text').extract_first()
        initial_courses_data['seminar_class_hours'] = response.css('div.views-field.views-field-field-course-tutorial-hours div.field-content::text').extract_first()
        initial_courses_data['laboratory_class_hours'] = response.css('div.views-field.views-field-field-course-lab-hours div.field-content::text').extract_first()
        initial_courses_data['eclass_link'] = response.css('div.field.field--name-field-eclass-link.field--type-link.field--label-inline a::attr(href)').extract_first()
        initial_courses_data['required'] = response.css('.views-field.views-field-field-course-prerequisites a::text').extract_first()
        initial_courses_data['recommended'] = response.css('.views-field.views-field-field-recommended-prerequisites a::text').extract_first()
        return initial_courses_data
