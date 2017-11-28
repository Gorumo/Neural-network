import scrapy
import re
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    global ALL_DATA
    ALL_DATA = []

    def start_requests(self):
        Openedu = json.load(open('Courses.json'))
        COURSE_URLS = []
        # Для обхода по всем курсам rang(len(Openedu))
        for i in range(len(Openedu)):
            try:
                url = "https://openedu.ru" + Openedu[str(i)]["url"]
                COURSE_URLS.append(url)
            except:
                pass

        for COURSE_URL in COURSE_URLS:
            yield scrapy.Request(url=COURSE_URL, callback=self.parse)

    def parse(self, response):
        course = {}
        # Ссылка
        course["URL"] = response.url
        title = response.xpath(
            '//h1[contains(@class,"course-title")]/text()').extract_first()
        course["Title"] = title
        # Направления подготовки
        directions = response.xpath(
            '//div[contains(@class, "groups")]//a/text()').extract()
        course["Directions"] = directions
        # Зачетные единицы
        credits = response.xpath(
            '//li[@class="clearfix" and position() = last()]').extract_first()
        credits = re.findall(r'\d+', credits)
        credits = int(''.join(str(i) for i in credits))
        course["Credits"] = credits
        # Компетенции
        competence = response.xpath("//h2[@id='result_knowledge']/following-sibling::ul").extract()
        for i in range(len(competence)):
            if "Уметь" or "Владеть" or "Знать" in competence[i]:
                competence.pop(i)
            mas = competence[i].split('</li>')
            if len(mas)>1:
                competence.pop(i)
                competence.extend(mas)
            mas = competence[i].split('</li>')
            if len(mas)>1:
                competence.pop(i)
                competence.extend(mas)
            mas = competence[i].split(';')
            if len(mas)>1:
                competence.pop(i)
                competence.extend(mas)
            mas = competence[i].splitlines()
            if len(mas)>1:
                competence.pop(i)
                competence.extend(mas)
        for i in range(len(competence)):        
            competence[i]=re.sub('<[^<]+?>', '', competence[i])
            competence[i]=re.sub(r'[\t\n\r]', '', competence[i])
        competence = list(filter(None, competence))
        course["Competence"] = competence
        ALL_DATA.append(course)
        with open('data.json', 'w') as f:
            json.dump(ALL_DATA, f, ensure_ascii=False)
        print(ALL_DATA)
