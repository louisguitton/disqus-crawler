to_crawl="http://www.purseblog.com/louis-vuitton/louis-vuitton-chanel-resort-2016-ad-campaigns/"
echo 'CRAWLING ...' $to_crawl
scrapy crawl url_grabber -a url=$to_crawl
Content="$(cat url.txt)"
echo 'CARJACKING ...' $Content
scrapy crawl json_grabber -a url=$Content
python get_posts.py
