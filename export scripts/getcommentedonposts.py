import json
import sys

post_ids = []
posts = {}

with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		post_id = comment["post"]["id"]
		if not post_id in post_ids and comment.get("author_name", "[unknown]") == 'CrystalVulpine':
			print("Post " + post_id)
			post_ids.append(post_id)

with open("submissions.f1.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		post = json.loads(jsonline)
		post_id = post["id"]
		if not post_id in post_ids and post.get("author_name", "[unknown]") == 'CrystalVulpine':
			print("Post " + post_id)
			post_ids.append(post_id)
		if post_id in post_ids:
			print("Writing Post " + post_id)
			posts[post_id] = jsonline

with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		post_id = comment["post"]["id"]
		if post_id in post_ids:
			if not post_id in posts:
				print("Writing Post " + post_id)
				posts[post_id] = json.dumps(comment["post"]) + "\n"
			posts[post_id] += jsonline
			print("Writing Comment in " + post_id)

for post_id in post_ids:
	with open("allposts/post_" + post_id + ".json", "w+") as af:
		print("Writing allposts/post_" + post_id + ".json")
		af.write(posts[post_id])
