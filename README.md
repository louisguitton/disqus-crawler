Blog Comments Crawler


What is it?
-----------
This project is a web crawler that can get and store the comments of a blog
if it is powered by DISQUS.

How is it done?
---------------

For the crawling, this project uses [scrapy](http://scrapy.org/).
It stores the comments in a MongoDB database, using the pymongo client.
A good tutorial to follow is [this one](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/).

When scrapping the web, 2 kind of problems kind arise:
- the target page is to slow to render because it uses a lot of javascript
- the target page renders everything really fast but what you were interested in was something that disappears when the page is renderred
To overcome these situations, one can deploy a tiy web-browser on a local machine
that will render the pages at his will.
This project uses Splash, on a local Docker container.
A good tutorial to follow is [this one](http://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash/).

Folder structure
--------------

--README.md                   The file you're looking at
--main.sh                     It calls the different jobs.
--get_posts.py                Called from main.sh. It takes care of MongoDB
--scrapy.cfg                  Nothing to report
--purseblog                   Folder create when running $scrapy startproject purseblog
----settings.py               Here you set up Splash
----pipelines.py              Nothing to report
----items.py                  Nothing to report
----__init__.py               Nothing to report
----spiders                   The folder containing the crawlers
------getDisqusUrl.py         The crawler in charge of the first job in main.sh
------getJson.py              The crawler in charge of the second job in main.sh
------__init__.py             Nothing to report

Installation
------------

- Clone the github repository and cd into it
- Open main.sh and change the url to the blog page you want to crawl
- Make sure a mongod instance is running on your computer
$ mongod
- Make sure a splash instance is running [(more information here)](https://github.com/scrapinghub/scrapy-splash)
$ docker run -p 8050:8050 scrapinghub/splash
- Run the main.sh script
$ sh main.sh

Contacts
--------

The author is [Louis Guitton](http://louisguitton.github.io)
