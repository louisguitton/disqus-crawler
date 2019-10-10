# coding=utf-8
import scrapy

# Define the Splash API endpoint
RENDER_HTML_URL = "http://localhost:8050/render.html"


class JsonGrabberSpider(scrapy.Spider):
    name = "json_grabber"

    # the crawler takes an URL in input
    # this URL is the output of the UrlGrabberSpider in getDisqusUrl.py
    def __init__(self, url):
        self.start_urls = [url]
        # An example URL could be:
        # http://disqus.com/embed/comments/?base=default&amp;version=afe1dd72cff7b0c7fecc0f7b3d92eb5e&amp;f=purseblog&amp;t_i=134117%20http%3A%2F%2Fwww.purseblog.com%2F%3Fp%3D134117&amp;t_u=http%3A%2F%2Fwww.purseblog.com%2Flouis-vuitton%2Flouis-vuitton-chanel-resort-2016-ad-campaigns%2F&amp;t_e=Feast%20Your%20Eyes%20on%20Bag-Heavy%20Cruise%202016%20Ads%20from%20Louis%20Vuitton%20and%20Chanel&amp;t_d=Feast%20Your%20Eyes%20on%20Bag-Heavy%20Cruise%202016%20Ads%20from%20Louis%20Vuitton%20and%20Chanel&amp;t_t=Feast%20Your%20Eyes%20on%20Bag-Heavy%20Cruise%202016%20Ads%20from%20Louis%20Vuitton%20and%20Chanel&amp;s_o=default&amp"

    # We use scrapy to and the Xpath syntax to extract information
    # We then store this inforamatino in a file called thread.json
    def parse(self, response):
        json = response.xpath("//script[@id='disqus-threadData']/text()").extract()[0]
        # Other ways of getting the same information would be:
        # response.xpath("//iframe[@title='Disqus']")
        # response.xpath("//iframe[contains(@id,'dsq')]")

        filename = 'thread.json'
        with open(filename, 'wb') as f:
            f.write(json)
