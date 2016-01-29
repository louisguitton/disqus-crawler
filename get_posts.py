fo = open("thread.json", "r+")
json_string = fo.read();
import json
parsed_json = json.loads(json_string)
posts = parsed_json["response"]["posts"]
# print len(posts)

#mongoimport --db disqus --collection posts --type json --file posts.json #--jsonArray
import pymongo
client = pymongo.MongoClient()
db = client.disqus
db.comments.insert_many(posts)
