# -*- coding: utf-8 -*-
import scrapy


class BiyingSpider(scrapy.Spider):
    name = 'biying'
    allowed_domains = ['www.bing.com']
    # 发送post请求不能使用原来的格式了
    # start_urls = ['http://www.bing.com/']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        post_url = 'https://www.bing.com/ttranslationlookup'
        data = {
            'from':'zh-CHS',
            'to':'en',
            'text':'狗',
        }

        yield scrapy.FormRequest(url=post_url,formdata=data,
                                 callback=self.parse_post)


    def parse_post(self,response):
        print(response.text)











