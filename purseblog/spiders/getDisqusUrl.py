# coding=utf-8
import scrapy

# Imports needed for talking to the Splash API
import json
from scrapy.http.headers import Headers

# Define the Splash API endpoint
RENDER_HTML_URL = "http://localhost:8050/render.html"


class UrlGrabberSpider(scrapy.Spider):
    name = "url_grabber"

    # the crawler takes an URL in input
    # so we put that in the initializer
    def __init__(self, url):
        self.start_urls = [url]

    # We call the Splash API as a middleware
    # to render the desired URL
    # In this casse we don't want the page to render all the javascript
    # So we set the js_enabled parameter to False
    def start_requests(self):
        for url in self.start_urls:
            body = json.dumps({"url": url, "wait": 0.5, "js_enabled": False })
            headers = Headers({'Content-Type': 'application/json'})
            yield scrapy.Request(RENDER_HTML_URL, self.parse, method="POST",
                                 body=body, headers=headers)

    # Then, as a callback from the Splash request,
    # we actually use scrapy and the Xpath syntax to extract information.
    # We then store this information into a file called url.txt
    def parse(self, response):
        iframe = response.xpath("//iframe[contains(@src,'http://disqus.com') or contains(@src,'https://disqus.com')]")
        # Other ways of getting the same information would be:
        # response.xpath("//iframe[@title='Disqus']")
        # response.xpath("//iframe[contains(@id,'dsq')]")
        url = iframe.xpath("@src").extract()[0]

        # Output to a file
        filename = 'url.txt'
        with open(filename, 'wb') as f:
            f.write(url)
