# coding=utf-8
import scrapy

import json
from scrapy.http.headers import Headers

from purseblog.items import DisqusUrlItem

import requests

RENDER_HTML_URL = "http://localhost:8050/render.html"


class UrlGrabberSpider(scrapy.Spider):
    name = "url_grabber"
    def __init__(self, url):
        self.start_urls = [url]

    '''
    allowed_domains = ["purseblog.com"]
    start_urls = ["http://www.purseblog.com/louis-vuitton/louis-vuitton-chanel-resort-2016-ad-campaigns/",
    "http://www.topgear.com/car-reviews/ct6/first-drive",
    "http://bgr.com/2016/01/28/apple-iphone-5se-release-date/"]
    start_urls2 = ["http://www.bikeexif.com/honda-cb900-custom",
    "http://thedissolve.com/news/6187-the-end/",
    "http://www.robsessedpattinson.com/2016/01/new-pics-robert-pattinson-debuts-his.html"]
    '''

    def start_requests(self):
        for url in self.start_urls:
            body = json.dumps({"url": url, "wait": 0.5, "js_enabled": False })
            headers = Headers({'Content-Type': 'application/json'})
            yield scrapy.Request(RENDER_HTML_URL, self.parse, method="POST",
                                 body=body, headers=headers)

    def parse(self, response):
        iframe = response.xpath("//iframe[contains(@src,'http://disqus.com') or contains(@src,'https://disqus.com')]")
        # response.xpath("//iframe[@title='Disqus']")
        # response.xpath("//iframe[contains(@id,'dsq')]")
        url = iframe.xpath("@src").extract()[0]

        '''
        # Implementation with items
        item = DisqusUrlItem()
        item["url"] = url
        yield item
        '''

        # Output to a file
        filename = 'url.txt'
        with open(filename, 'wb') as f:
            f.write(url)
