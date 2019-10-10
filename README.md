# disqus-crawler

> Crawl DISQUS comments from a blog into a local MongoDB database

## Installation

- Clone the github repository and cd into it

```bash
git clone git@github.com:louisguitton/disqus-crawler.git
cd disqus-crawler
python3 -m venv venv
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

## Usage example

- Open main.sh and change the url to the blog page you want to crawl
- Make sure a mongod instance is running on your computer (Installation instructions for MongoDB are [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/))

```bash
mongod --config /usr/local/etc/mongod.conf
```

- Make sure a splash instance is running [(more information here)](https://github.com/scrapinghub/scrapy-splash)

```bash
$ docker run -p 8050:8050 scrapinghub/splash
2019-10-10 12:03:39.116598 [-] Server listening on http://0.0.0.0:8050
```

- Run the main.sh script

```bash
$ sh main.sh
CRAWLING ... http://www.purseblog.com/louis-vuitton/louis-vuitton-spring-2016-bag-ad-campaign/
2019-10-10 14:07:28 [scrapy.utils.log] INFO: Scrapy 1.7.3 started (bot: purseblog)
...
```

- Usage

```bash
mongo
```

```mongodb
use disqus
db.comments.count()
db.comments.find().pretty().limit(2)
```

## Meta

I wrote this project for my master thesis in 2016 on Paid/Owned/Earned Media, and measuring brands on social channels and blogs.

For the crawling, this project uses [scrapy](http://scrapy.org/).
It stores the comments in a MongoDB database, using the pymongo client.
A good tutorial to follow is [this one](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/).

When scrapping the web, 2 kinds of problems arise:

- the target page is too slow to render because it uses a lot of javascript
- the target page renders everything really fast but what you were interested in was something that disappears when the page is rendered

To overcome these situations, one can deploy a tiny web-browser on a local machine
that will render the pages at his will.
This project uses Splash, on a local Docker container.
A good tutorial to follow is [this one](http://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash/).
