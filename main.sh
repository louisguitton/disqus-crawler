# Choose the blog article you want to crawl
# NOTE: the blog should be powered by DISQUS
to_crawl="http://www.purseblog.com/louis-vuitton/louis-vuitton-spring-2016-bag-ad-campaign/"

# Get the API call from the blog post to DISQUS
# Save this link in a file called "url.txt"
echo 'CRAWLING ...' $to_crawl
venv/bin/scrapy crawl url_grabber -a url=$to_crawl
Content="$(cat url.txt)"

# Crawl the JSON file the API is sending back
# Save this to a file called "thread.json"
echo 'CARJACKING ...' $Content
venv/bin/scrapy crawl json_grabber -a url=$Content

# Save the comments to a MongoDB database disqus.comments
venv/bin/python get_posts.py
