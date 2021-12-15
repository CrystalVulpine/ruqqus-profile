import json
import sys

post_ids = []

with open("ruqqus.submf.2021-10-14.json", "r") as f:
	for jsonline in f:
		post = json.loads(jsonline)
		post_id = post["id"]
		if not post_id in post_ids:
			post_ids.append(post_id)

with open("myposts-html.json", "r") as f, open("missingposts-html.json", "w+") as af:
	line = 0
	for jsonline in f:
		line += 1
		try:
			post = json.loads(jsonline)
		except:
			print("Error: " + str(line))
			break
		post_id = post["item_id_alias"]
		if not post_id in post_ids and post.get("author", "[unknown]") == '@CrystalVulpine':
			print("Missing " + post_id + "\n")
			af.write(jsonline)
