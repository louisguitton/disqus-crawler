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
