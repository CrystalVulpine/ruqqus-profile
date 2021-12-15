import json
import sys

post_ids = []

with open("myposts.json", "r") as f:
	for jsonline in f:
		post = json.loads(jsonline)
		post_id = post["id"]
		if not post_id in post_ids:
			post_ids.append(post_id)

with open("postsfromcomments.json", "r") as f, open("missingposts.json", "w+") as af:
	for jsonline in f:
		post = json.loads(jsonline)
		post_id = post["id"]
		if not post_id in post_ids:
			print("Missing " + post_id + "\n")
			af.write(jsonline)
