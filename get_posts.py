import json
import pymongo

with open("thread.json", "r+") as fo:
    json_string = fo.read()

parsed_json = json.loads(json_string)
posts = parsed_json["response"]["posts"]

client = pymongo.MongoClient()
db = client.disqus
db.comments.insert_many(posts)
